from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
app = Flask(__name__)
# Turn on Cross Origin Resource Sharing (CORS) for all requests
CORS(app)

#'POST' or 'GET' request under the URL => http://127.0.0.1:5000/data
@app.route('/data', methods=['GET', 'POST'])
def login():
    #Just test data
    data = [
        {"content":"mochulskyy.com"},
        {"content":"some other "},
        {"content":"just"}
    ]

    #Request 'GET'
    if request.method == 'GET':
        return jsonify(data);

    #Request 'POST'
    elif request.method == 'POST':
        return jsonify(content= 'mochulskyy.com', time= '10:00')


if __name__ == "__main__":
    app.run(debug=True)


# Activate flask => '. venv/bin/activate'
