from flask.ext.restful import reqparse
import json
from flask import request, abort, jsonify
from flask.ext import restful
from bson.objectid import ObjectId
from restful_service import app, api, mongo

class ExperimentList(restful.Resource):
    def __init__(self, *args, **kwargs):
        super(ExperimentList, self).__init__()

# show all the experiment list
    def get(self):
        return  [x for x in mongo.db.experiments.find()]

# post a experiment to the web
    def post(self):
        experiment_data = request.get_json()
        experiment_form = experiment_data['form']
        experiment_users = experiment_data['users']
        data = json.dumps(experiment_data)
        experiment_id = mongo.db.experiments.insert(experiment_data)
        return mongo.db.experiments.find_one({"_id": experiment_id})

# the method could be used to modify get new and delete item experiment the list
class Experiment(restful.Resource):
    def get(self, experiment_id):
        # return mongo.db.users.find_one_or_404({"": })
        return mongo.db.experiments.find_one_or_404({"_id": experiment_id})

    def delete(self, experiment_id):
        mongo.db.experiments.find_one_or_404({"_id": experiment_id})
        mongo.db.experiments.remove({"_id": experiment_id})
        return '', 204

    def put(self, experiment_id):
        target_id = {'_id': experiment_id}
        update_content = {'$set': request.get_json()}
        mongo.db.experiments.update_one(target_id, update_content, upsert=False)
        return mongo.db.experiments.find_one_or_404({"_id": experiment_id})


api.add_resource(ExperimentList, '/experiments/')
api.add_resource(Experiment, '/experiments/<ObjectId:experiment_id>')
