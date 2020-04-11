from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
# Turn on Cross Origin Resource Sharing (CORS) for all requests
CORS(app)


@app.route('/data', methods=['GET', 'POST'])
def login():
    data = [
        {"content":"mochulskyy.com"},
        {"content":"some other "},
        {"content":"just"}
    ]

    if request.method == 'GET':
        return jsonify(data);

    elif request.method == 'POST':
        return jsonify(content= 'mochulskyy.com', time= '10:00')


if __name__ == "__main__":
    app.run(debug=True)


# Activate flask => '. venv/bin/activate'
