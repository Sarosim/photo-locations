import os 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app=Flask(__name__)

app.config["MONGO_DBNAME"]='photo_locations'
app.config['MONGO_URI']='mongodb+srv://nick:n1ckUser@myfirstcluster-mbpma.mongodb.net/photo_locations?retryWrites=true&w=majority'
mongo=PyMongo(app)

@app.route('/')
def index():
    return redirect(url_for('landing'))
    
@app.route('/landing')
def landing():
    return render_template('landing.html', entries=mongo.db.details.find())
    
@app.route('/add_location')    
def add_location():
    return render_template('addlocation.html', categories=mongo.db.categories.find())
    
@app.route('/insert_location', methods=['POST'])
def insert_location():
    entries=mongo.db.details
    entries.insert_one(request.form.to_dict())
    return redirect(url_for('landing'))
    
@app.route('/display_details')
def display_details():
    return render_template('details.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)    