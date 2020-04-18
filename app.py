from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps
app = Flask(__name__)

#Connect to the local MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/qr_data"
mongo = PyMongo(app)

# Turn on Cross Origin Resource Sharing (CORS) for all requests
CORS(app)

#'POST' or 'GET' request under the URL => http://127.0.0.1:5000/qr_data
@app.route('/qr_data', methods=['GET', 'POST'])
def backend_request():
    #Database colletion to insert onto
    qr_collection = mongo.db.qr_collection;

    if request.method == 'GET':
        #Get the collection from the database
        collection = dumps(qr_collection.find());

        #Return JSON object
        return collection;

    elif request.method == 'POST':
        #Get URL-parameter
        urlValueData = request.args.get('data')
        urlValueDate = request.args.get('date')
        urlValueTime = request.args.get('time')
        #Check if it is 'none' or 'empty'
        if urlValueData is not None and urlValueData != '' and urlValueDate is not None and urlValueDate != '' and urlValueTime is not None and urlValueTime != '':
            collectionData = {'data': urlValueData, 'date': urlValueDate, 'time': urlValueTime}

            #Insert the URL-parameter value into the database
            qr_collection.insert_one(collectionData);
            return "Successful";
        else: 
            return "Unsuccessful";

#Just for debug purposes
if __name__ == "__main__":
    app.run(debug=True)

# Activate flask => '. venv/bin/activate'
# Start => 'python3 app.py'
