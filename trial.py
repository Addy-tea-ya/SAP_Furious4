from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from json import JSONEncoder
import copy
import pymongo
from pymongo import MongoClient
app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def create_task():
    print("hi")
    if not request.json or not 'junction1' in request.json:
        abort(400)
    task = {
        'junction1': request.json['junction1'],
    }
    print(task['junction1'])
    cluster=MongoClient("mongodb+srv://SAP:aditya@cluster0.7sekq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db=cluster["myFirstDatabase"]
    collection = db["junction1"]
    ls=[]
    for x in collection.find():
        ls=[str(x["Lane1"]),str(x["Lane2"]),str(x["Lane3"]),str(x["Lane4"])]
    print(ls)
    task['junction1']=ls
    print("Done")
    return jsonify({'task': task}), 201
@app.route("/about")
def about():
    return render_template('team.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')
CORS(app)
if __name__ == '__main__':
    app.run()
