#!flask/bin/python
from flask import Flask, jsonify
from getTrends import getTrends

app = Flask(__name__)

@app.route('/')
def get_trends():
    return jsonify(getTrends()) 

if __name__ == '__main__':
    app.run(debug=True)
