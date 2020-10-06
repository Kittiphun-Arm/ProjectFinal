from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS 

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'DATAPROJECT'
app.config['MONGO_URI'] = 'mongodb+srv://admin:68276728@projectdisasterrisk.wh8co.gcp.mongodb.net/DATAPROJECT?retryWrites=true&w=majority'

mongo = PyMongo(app)
CORS(app)

@app.route('/dataDisaster', methods=['GET'])
def get_all_tasks():
    dataDisaster = mongo.db.dataDisaster 
    result = []
    for field in dataDisaster.find():
        result.append({'_id': str(field['_id']), 'score': field['score'],'disaster': field['disaster'],'province': field['province']})
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)