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
    return 'Hello World'
    
@app.route('/landing')
def landing():
    return render_template('landing.html', entries=mongo.db.photo_locations.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)    