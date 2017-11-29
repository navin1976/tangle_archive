from flask import Blueprint, jsonify

from models import Transactions
from models.Transactions import TransactionModel

api = Blueprint("api", __name__)



@api.route("/")
def index():
    return "Hello Cassandra.."


@api.route("/<string:hashInput>")
def hashExists(hashInput):
    result = TransactionModel.objects(hash=hashInput)
    if result.count() > 0:
        return jsonify({"exists": "true", "count":result.count()})
    else:
        return jsonify({"exists": "false" , "count":result.count()})

@api.route("/address/<string:addressInput>")
def addressExists(addressInput):
    result = TransactionModel.objects(address=addressInput)
    if result.count() > 0:
        return jsonify({"exists": "true", "count":result.count()})
    else:
        return jsonify({"exists": "false" , "count":result.count()})