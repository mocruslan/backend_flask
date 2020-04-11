from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps
app = Flask(__name__)

#Connect to the local MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/qr_data"
mongo = PyMongo(app)

# Turn on Cross Origin Resource Sharing (CORS) for all requests
CORS(app)

#'POST' or 'GET' request under the URL => http://127.0.0.1:5000/data
@app.route('/qr_data', methods=['GET', 'POST'])
def backend_request():
    #Database colletion to insert onto
    qr_collection = mongo.db.qr_collection;

    #Request 'GET'
    if request.method == 'GET':
        #Get the collection from the database
        collection = dumps(qr_collection.find());

        #Return JSON object
        return collection;

    #Request 'POST'
    elif request.method == 'POST':
        #Get URL-parameter
        url_value = request.args.get('content')

        #Check if it is 'none' or 'empty'
        if url_value is not None and url_value != '':
            #print('----Value is: ' + url_value);
            qr_value = {'content': url_value};
            #Insert the URL-parameter value into the database
            qr_collection.insert_one(qr_value);
            return "True";
        else: 
            return "False";

#Just for debug purposes
if __name__ == "__main__":
    app.run(debug=True)

# Activate flask => '. venv/bin/activate'
