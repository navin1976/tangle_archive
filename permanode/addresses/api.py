from flask import jsonify, abort
from cassandra.cqlengine.query import DoesNotExist, BatchQuery
from cassandra.cqlengine.query import MultipleObjectsReturned
from permanode.addresses import addresses
from permanode.models import AddressModel,AddressTokenReceivedModel


@addresses.route('/addresses/<address>', methods=['GET'])
def validate_address_usage(address):
    return jsonify({ 'is_spent': True, 'address': address })


@addresses.route('/addresses/spent/<address>') # TODO: Sort out route names
def verify_address_usage(address):
    result = AddressModel.objects(address=address)

    if not result.count():
        abort(404)

    spent_from_query = result.filter(value__lt=0)

    spent = False

    try:
        spent_from_query.get()
        spent = True
    except DoesNotExist as e:
        spent = False
    except MultipleObjectsReturned as m:
        spent = True

    return jsonify({'spent': spent})


@addresses.route('/addresses/unique', methods=['GET'])
def fetch_unique_addresses():
    result = AddressModel.objects().distinct()
    return jsonify({'addresses': result.count()})

@addresses.route("/addresses/tokenReceived/<string:addressInput>")
def fetch_tokans_received_by_address(addressInput):
    result = AddressTokenReceivedModel.objects(address=addressInput)
    return jsonify([res.get_transaction_token_received_data() for res in result])

