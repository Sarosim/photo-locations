import os 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import time
import datetime

app=Flask(__name__)

app.config["MONGO_DBNAME"]='photo_locations'
app.config['MONGO_URI']='mongodb+srv://nick:n1ckUser@myfirstcluster-mbpma.mongodb.net/photo_locations?retryWrites=true&w=majority'
mongo=PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    entries = mongo.db.details.find()
    locations = []
    location = {}
# Creating the dictionary of the locations to pass to the Google map API
    for entry in entries:
# because of the schema wasn't set up properly at the beginning, the database contains mixed types for lat/lon (as well as recods without...), so I have to check for type
        if 'lat' in entry:
            if isinstance(entry['lat'], str):
                location['lat'] = float(entry['lat'])
                location['lng'] = float(entry['lon'])
            else:
                location['lat'] = entry['lat']
                location['lng'] = entry['lon']
            locations.append(location)
        print('9******************************************************************************************************************************')    
        print(type(locations))
    return render_template('index.html', counter = mongo.db.details.find().count(), locs = locations)
    
@app.route('/landing')
def landing():
    return render_template('landing.html', entries = mongo.db.details.find().sort([('date_modified', -1)]))
    
@app.route('/add_location')    
def add_location():
    return render_template('addlocation.html', categories=mongo.db.categories.find())
    
@app.route('/insert_location', methods=['POST'])
def insert_location():
    entries=mongo.db.details
    new_id = entries.insert_one(request.form.to_dict()).inserted_id
#    new_entry = entries.find_one({'_id': new_id})
    entries.update({'_id': new_id},
        {'$currentDate': {'date_modified': True }})
    return redirect(url_for('landing'))
    
@app.route('/display_details/<rec_id>')
def display_details(rec_id):
    the_record = mongo.db.details.find_one({"_id": ObjectId(rec_id)})
    entries=mongo.db.details
# This is the previous workaround, I'm keeping it here for a while, the syntax might help with other solutions...
#    if 'num_of_views' in the_record:
 #       prev_num_views = mongo.db.details.find_one({"_id": ObjectId(rec_id)})['num_of_views']
  #      new_num_views = prev_num_views + 1
    #else:
   #     new_num_views = 1
    #entries.update({'_id': ObjectId(rec_id)},
     #   {'$set': {'num_of_views': new_num_views}})
    entries.update({'_id': ObjectId(rec_id)}, {'$inc': {'num_of_views': 1}})
    category_list = mongo.db.categories.find()
    return render_template('details.html', record = the_record, categories = category_list)
    
@app.route('/edit_record/<record_id>')
def edit_record(record_id):
    the_record = mongo.db.details.find_one({"_id": ObjectId(record_id)})
    category_list = mongo.db.categories.find()
    return render_template('updatelocation.html', record = the_record, categories = category_list)
    
@app.route('/save_updates/<record_id>', methods=["POST"])
def save_updates(record_id):
    timestamp = datetime.datetime.utcnow()
    details = mongo.db.details
    details.update({'_id': ObjectId(record_id)},
    {
        'title': request.form.get('title'),
        'category_name': request.form.get('category_name'),
        'country': request.form.get('country'),
        'region': request.form.get('region'),
        'post_code': request.form.get('post_code'),
        'lat': request.form.get('lat'),
        'lon': request.form.get('lon'),
        'camera': request.form.get('camera'),
        'lens': request.form.get('lens'),
        'filters': request.form.get('filters'),
        'photographer': request.form.get('photographer'),
        'tripod_used': request.form.get('tripod_used'),
        'description': request.form.get('description'),
        'image_url': request.form.get('image_url'),
        'date_modified': timestamp
    })
    return redirect(url_for('landing'))
    
@app.route('/add_like/<record_id>', methods=['GET','POST'])
def add_like(record_id):
    the_record = mongo.db.details.find_one({"_id": ObjectId(record_id)})
    entries=mongo.db.details
    entries.update({'_id': ObjectId(record_id)}, {'$inc': {'num_of_likes': 1}})
    category_list = mongo.db.categories.find()
    return render_template('details.html', record = the_record, categories = category_list)
    
    
@app.route('/delete_record/<record_id>')
def delete_record(record_id):
    mongo.db.details.remove({'_id': ObjectId(record_id)})
    return redirect(url_for('landing'))
    
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)    