from flask import Flask
import os 

app=Flask(__name__)


@app.route('/')
def landing_page():
    return 'Hello World'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)    