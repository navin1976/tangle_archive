from cassandra import cqlengine
from flask import Blueprint, jsonify

from models.Approvee_model import ApproveeModel
from cassandra.cqlengine.query import DoesNotExist, BatchQuery
from cassandra.cqlengine.query import MultipleObjectsReturned

api = Blueprint("api", __name__)

@api.route("/approvee-search/<string:hashinput>", methods=['GET'])
def get_approvee(hashinput):
    result = ApproveeModel.objects(hash=hashinput)
    return jsonify([res.get_approvee_hash() for res in result])
    
