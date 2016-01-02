from flask.ext.restful import reqparse
import json
from flask import request, abort, jsonify
from flask.ext import restful
from bson.objectid import ObjectId
from restful_service import app, api, mongo

class ResultList(restful.Resource):
    def __init__(self, *args, **kwargs):
        super(ResultList, self).__init__()

# show all the result list
    def get(self):
        return  [x for x in mongo.db.results.find()]

# post a result to the web
    def post(self):
        result_data = request.get_json()
        result_user = result_data['user']
        result_time = result_data['time']
        result_title = result_data['title']
        result_content = result_data['content']
        data = json.dumps(result_data)
        result_id = mongo.db.results.insert(result_data)
        return mongo.db.results.find_one({"_id": result_id})

# the method could be used to modify get new and delete item result the list
class Result(restful.Resource):
    def get(self, result_id):
        # return mongo.db.users.find_one_or_404({"": })
        return mongo.db.results.find_one_or_404({"_id": result_id})

    def delete(self, result_id):
        mongo.db.results.find_one_or_404({"_id": result_id})
        mongo.db.results.remove({"_id": result_id})
        return '', 204

    def put(self, result_id):
        target_id = {'_id': result_id}
        update_content = {'$set': request.get_json()}
        mongo.db.results.update_one(target_id, update_content, upsert=False)
        return mongo.db.results.find_one_or_404({"_id": result_id})


api.add_resource(ResultList, '/results/')
api.add_resource(Result, '/results/<ObjectId:result_id>')
