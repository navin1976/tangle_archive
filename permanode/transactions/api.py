from flask import jsonify
from permanode.transactions import transactions
from permanode.models import AddressModel, TransactionModel,TagModel,valueModel


@transactions.route('/transactions/address/<address>', methods=['GET'])
def fetch_transactions_by_address(address):
    result = AddressModel.objects(address=address).limit(10)

    return jsonify([res.get_address_data() for res in result])


@transactions.route('/transactions/hash/<transaction_hash>', methods=['GET'])
def verify_transaction_existence(transaction_hash):
    result = TransactionModel.objects(hash=transaction_hash)
    
    return jsonify([res.get_transaction_data() for res in result])

@transactions.route('/transactions/tag/<tagInput>', methods=['GET'])
def fetch_transactions_by_tag(tagInput):
    result = TagModel.objects(tag=tagInput)

    return jsonify([res.get_tag_data() for res in result])
@transactions.route('/values/')
def fetch_value_counts():
    result = valueModel.objects()
    return jsonify([res.get_value_data() for res in result])