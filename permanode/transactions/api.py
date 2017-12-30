from flask import jsonify, abort
from permanode.transactions import transactions
from permanode.models import AddressModel, TransactionModel,TagModel,BundleHashModel,TransactionApproveeModel
from permanode.shared.iota_api import IotaApi

@transactions.route('/transactions/exists/<transaction_hash>', methods=['GET'])
def verify_transaction_existence(transaction_hash):
    result = TransactionModel.objects(hash=transaction_hash)

    if result.count():
        return jsonify({'exists': True})
    return jsonify({'exists': False})

@transactions.route('/transactions/address/<address>', methods=['GET'])
def fetch_transactions_by_address(address):
    result = AddressModel.objects(address=address).limit(10)
    if result.count():
        return result
    else:
        return None
@transactions.route('/transactions/hash/approvees/<transaction_hash>',methods=['GET'])
def fetch_transaction_approvees(transaction_hash):
    result = TransactionApproveeModel.objects(hash=transaction_hash)
    # return jsonify([res.get_transaction_approvee_data() for res in result])
    if result.count():
        return result
    else:
        return None

@transactions.route('/transactions/hash/<transaction_hash>', methods=['GET'])
def fetch_transactions_by_hash(transaction_hash):
    result = TransactionModel.objects(hash=transaction_hash).limit(10)

    if result.count():
        return result
    else:
        return None

@transactions.route('/transactions/bundle/<bundle>', methods=['GET'])
def fetch_transactions_by_bundleHash(transaction_bundle_hash):
    result = BundleHashModel.objects(bundle_hash=transaction_bundle_hash)
    if result.count():
        return result
    return None

@transactions.route('/transactions/tag/<transaction_tag>', methods=['GET'])
def fetch_transactions_by_tag(transaction_tag):
    result = TagModel.objects(tag=transaction_tag)
    
    if result.count():
        return result
    else:
        return None