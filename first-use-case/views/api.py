from flask import Blueprint, jsonify

from models.AddressModel import AddressModel
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

@api.route("/get-address-count/<string:addressInput>")
def addressExists(addressInput):
    result = AddressModel.objects(address=addressInput)
    if result.count() > 0:
        return jsonify({"exists": "true", "count":result.count()})
    else:
        return jsonify({"exists": "false" , "count":result.count()})

@api.route("/get-transaction-by-address/<string:addressInput>")
def getTransactionByAddress(addressInput):
    result = AddressModel.objects(address=addressInput)
    return jsonify([res.get_address_data() for res in result])

