import os 
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import time
import datetime

app=Flask(__name__)

app.config["MONGO_DBNAME"]='photo_locations'
app.config['MONGO_URI']='mongodb+srv://nick:n1ckUser@myfirstcluster-mbpma.mongodb.net/photo_locations?retryWrites=true&w=majority'
mongo=PyMongo(app)

# Helper function for eliminating inconsistencies in the tripod_used field:
def fix_tripod():
    entries = mongo.db.details.find()
    details = mongo.db.details
    for entry in entries:
        print("ID: ")
        print(entry['_id'])
        print("tripod_used: ")
        print(entry["tripod_used"])
        #If it contains tripod field
        if "tripod_used" in entry:
            if entry["tripod_used"] == "on":
                entry["tripod_used"] = True
            if entry["tripod_used"]  == "":
                entry["tripod_used"]  = False
            if entry["tripod_used"]  == None:
                entry["tripod_used"]  = False    
        
        #If it doesn't contain tripod_used field
        else:
            entry["tripod_used"] = False
        details.update_one({'_id': entry['_id']},
        {
            "$set": {"tripod_used": entry["tripod_used"]}
        })
fix_tripod()

@app.route('/')
@app.route('/index')
def index():
    entries = mongo.db.details.find()
    location = {}
    data_to_send_to_map = {}
    data_to_send_all = []
# Creating the dictionary of the locations to pass to the Google map API
    for entry in entries:
# because of the schema wasn't set up properly at the beginning, the database contains mixed types for lat/lon (as well as documents without...), so I have to check for existance and type
        if "lat" in entry:
            if isinstance(entry["lat"], str):
                location["lat"] = float(entry["lat"])
                location["lng"] = float(entry["lon"])
            else:
                location["lat"] = float(str(entry["lat"])) #has to be in a format JSON can sterilize (Decimal128 is not), Float can not take decimal128 as argument either...
                location["lng"] = float(str(entry["lon"]))
            clone_of_location = location.copy()
# On top of the coordinates, I send more info 
            data_to_send_to_map["id"] = str(entry["_id"])
            data_to_send_to_map["cat"] = entry['category_name']
            data_to_send_to_map["title"] = entry["title"]
            data_to_send_to_map["point"] = clone_of_location
            clone_of_data = data_to_send_to_map.copy()
            data_to_send_all.append(clone_of_data)
#   convert into JSON: 
#   y = json.dumps(locations) THIS WASN'T needed in my case, as I convert on the javaScript side with: |tojson
    return render_template('index.html', counter = mongo.db.details.find().count(), data_source = data_to_send_all) 



# The Landing page where filtering and search can be performed, locations are diplayed in cards with primary info.    
@app.route('/landing')
def landing():
    # Creating the list of countries for the dropdown
    countries = []
    entries = mongo.db.details.find()
    for entry in entries:
        the_country = entry['country'].title() #capitalising each word in the country name to display nicely and avoid duplications
  #      print(the_country)
        if the_country not in countries:
            countries.append(the_country)
    countries.sort()
    # getting the categories for the dropdown
    category_list = mongo.db.categories.find()
    return render_template('landing.html', entries = mongo.db.details.find().sort([('date_modified', -1)]), countries = countries, categories = category_list)



# Filtering based on input from landing page 
@app.route('/filtering/<search_param>')
def filtering(search_param):
    print(search_param)
    return redirect(url_for('index'))
    


# Displaying the form to be filled for adding a new location
@app.route('/add_location')    
def add_location():
    return render_template('addlocation.html', categories=mongo.db.categories.find())



# Inserting the new document into the details collection     
@app.route('/insert_location', methods=['POST'])
def insert_location():
    entries=mongo.db.details
    # inserting and retrieving the _id tha was generated at insertion
    new_id = entries.insert_one(request.form.to_dict()).inserted_id
    # "initializing" the date_modified and the num_of_views, num_of_likes fields
    entries.update({'_id': new_id},
    {
        '$currentDate': {'date_modified': True},
        '$set': {'num_of_views': 0,
                'num_of_likes': 0}        
    })
    return redirect(url_for('landing'))
    


# Displaying the selected location's details and the picture      
@app.route('/display_details/<rec_id>')
def display_details(rec_id):
    entries=mongo.db.details
    #Incrementing the number of views for the selected/displayed location
    entries.update({'_id': ObjectId(rec_id)}, {'$inc': {'num_of_views': 1}})
    the_record = mongo.db.details.find_one({"_id": ObjectId(rec_id)})
    category_list = mongo.db.categories.find()
    return render_template('details.html', record = the_record, categories = category_list)



# Rendering the form for editing a record    
@app.route('/edit_record/<record_id>')
def edit_record(record_id):
    the_record = mongo.db.details.find_one({"_id": ObjectId(record_id)})
    category_list = mongo.db.categories.find()
    return render_template('updatelocation.html', record = the_record, categories = category_list)
    


# Saving the form data from the Edit feature
@app.route('/save_updates/<record_id>', methods=["POST"])
def save_updates(record_id):
    timestamp = datetime.datetime.utcnow()
    details = mongo.db.details
    the_record = mongo.db.details.find_one({"_id": ObjectId(record_id)})
    #I have to check whether the num_of_views and/or num_of_likes fields exist, because these were later introduced therefore not all documents have these fields
    if "num_of_views" in the_record:
        #Setting its value to rewrite to the document
        views = int(the_record["num_of_views"])
    else:
        #Setting it to zero if din't exist
        views = 0
    if "num_of_likes" in the_record:
        likes = int(the_record["num_of_likes"])
    else:
        likes = 0

    #I have to check the content of tripod_used fields exist, because these were later introduced therefore not all documents have these fields


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
        'date_modified': timestamp,
        'num_of_views': views,
        'num_of_likes': likes,
    })
    return redirect(url_for('landing'))



# Increasing the number of likes 
@app.route('/add_like/<record_id>', methods=['GET','POST']) #NO NEED FOR POST I GUESS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def add_like(record_id):
    entries=mongo.db.details
    entries.update({'_id': ObjectId(record_id)}, {'$inc': {'num_of_likes': 1}})
    #Because of redirecting to the display_details page, the number of views will be incremented there.
    #To compensate it, I decrease the num of views by 1 here, because it is not a new viewing of the page:
    entries.update({'_id': ObjectId(record_id)}, {'$inc': {'num_of_views': -1}})
    category_list = mongo.db.categories.find()
    the_record = mongo.db.details.find_one({"_id": ObjectId(record_id)})
    return redirect(url_for('display_details', rec_id = record_id))
    


# Deleting the selected document from the collection    
@app.route('/delete_record/<record_id>')
def delete_record(record_id):
    mongo.db.details.remove({'_id': ObjectId(record_id)})
    return redirect(url_for('landing'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)    