from flask.ext.restful import reqparse
import json
from flask import request, abort, jsonify
from flask.ext import restful
from bson.objectid import ObjectId
from restful_service import app, api, mongo

class UserList(restful.Resource):
    def __init__(self, *args, **kwargs):
        super(UserList, self).__init__()

# show all the user list
    def get(self):
        return  [x for x in mongo.db.users.find()]

# post a user to the web
    def post(self):
        user_data = request.get_json()
        name = user_data['name']
        email = user_data['email']
        gender = user_data['gender']
        job = user_data['job']
        mobile_os = user_data['mobile_os']
        mobile_name = user_data['mobile_name']
        pc_os = user_data['pc_os']
        data = json.dumps(user_data)
        user_id = mongo.db.users.insert(user_data)
        return mongo.db.users.find_one({"_id": user_id})

# the method could be used to modify get new and delete item user the list
class User(restful.Resource):
    def get(self, user_id):
        # return mongo.db.users.find_one_or_404({"": })
        return mongo.db.users.find_one_or_404({"_id": user_id})

    def delete(self, user_id):
        mongo.db.users.find_one_or_404({"_id": user_id})
        mongo.db.users.remove({"_id": user_id})
        return '', 204

    def put(self, user_id):
        target_id = {'_id': user_id}
        update_content = {'$set': request.get_json()}
        mongo.db.users.update_one(target_id, update_content, upsert=False)
        return mongo.db.users.find_one_or_404({"_id": user_id})


api.add_resource(UserList, '/users/')
api.add_resource(User, '/users/<ObjectId:user_id>')
