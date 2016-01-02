from flask.ext.restful import reqparse
import json
from flask import request, abort, jsonify
from flask.ext import restful
from bson.objectid import ObjectId
from restful_service import app, api, mongo

class FormList(restful.Resource):
    def __init__(self, *args, **kwargs):
        # self.parser = reqparse.RequestParser()
        # self.parser.add_argument('name', type=str)
        # self.parser.add_argument('description', type=str)
        # self.parser.add_argument('notification', type=str)
        # self.parser.add_argument('time', type=str)
        # self.parser.add_argument('question_set', type=str)
        super(FormList, self).__init__()

# show all the form list
    def get(self):
        return  [x for x in mongo.db.forms.find()]

# post a form to the web
    def post(self):
        form_data = request.get_json()
        # form_data = json.load()
        name = form_data['name']
        desc = form_data['description']
        noti = form_data['notification']
        start = form_data['start']
        end = form_data['end']
        ques = form_data['question_set']
        data = json.dumps(form_data)

        # for que in ques:
        #     print que["type"]
        #     print que["title"]
        # print type(form_data)
        # print type(desc)
        # print json.loads(ques)
        # print type(ques)
        # print form_data["question_set"][0]
        form_id = mongo.db.forms.insert(form_data)
        return mongo.db.forms.find_one({"_id": form_id})

# the method could be used to modify get new and delete item form the list
class Form(restful.Resource):
    def get(self, form_id):
        # return mongo.db.forms.find_one_or_404({"": })
        return mongo.db.forms.find_one_or_404({"_id": form_id})

    def delete(self, form_id):
        mongo.db.forms.find_one_or_404({"_id": form_id})
        mongo.db.forms.remove({"_id": form_id})
        return '', 204

    def put(self, form_id):
        target_id = {'_id': form_id}
        update_content = {'$set': request.get_json()}
        mongo.db.forms.update_one(target_id, update_content, upsert=False)
        return mongo.db.forms.find_one_or_404({"_id": form_id})

class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK'
        }

api.add_resource(Root, '/')
api.add_resource(FormList, '/forms/')
api.add_resource(Form, '/forms/<ObjectId:form_id>')
