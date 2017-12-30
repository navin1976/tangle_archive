from flask import jsonify, abort
from iota import Address, Bundle, Transaction, TryteString, Tag
from permanode.search import search
from permanode.shared.iota_api import IotaApi
import logging
from permanode.transactions import api as lookup_api 

@search.route('/<search_string>', methods=['GET'])
def fetch_associated_info(search_string):
    if not search_string or len(search_string) > 90:
        abort(400)

    api = IotaApi()


    if len(search_string) <= 27:
        result = lookup_api.fetch_transactions_by_tag(search_string)
        all_transaction_objects = []
        if result is not None:
            # return jsonify({
            #     'type': 'tag',
            #     'payload': [res.get_tag_data() for res in result]
            # })
            for res in result :
                all_transaction_objects.append(res.get_tag_data())

        tags, tags_status_code = api.find_transactions(tags=[search_string])

        if tags_status_code == 503 or tags_status_code == 400:
            return jsonify({
                'type': 'tag',
                'payload': all_transaction_objects
            })
            # abort(tags_status_code)
        elif tags_status_code == 200:
            if not tags['hashes']:
                return jsonify({
                    'type': 'tag',
                    'payload': all_transaction_objects
                })

            transaction_trytes, transaction_trytes_status_code = api.get_trytes(tags['hashes'])
            
        
        

            # for tryte in transaction_trytes['trytes']:
            #     tag_inst = Tag.from_tryte_string(tryte)

            #     all_transaction_objects.append(tag_inst.as_json_compatible())

            return jsonify({
                'type': 'tag',
                'payload': all_transaction_objects
            })

        return jsonify({
            'type': 'tag',
            'payload': []
        })

    if len(search_string) == 90:
        addresses, addresses_status_code = api.find_transactions(addresses=[search_string[:-9]])

        if addresses_status_code == 503 or addresses_status_code == 400:
            abort(addresses_status_code)
        elif addresses_status_code == 200:
            if not addresses['hashes']:
                return jsonify({
                    'type': 'address',
                    'payload': []
                })

            transaction_trytes, transaction_trytes_status_code = api.get_trytes(addresses['hashes'])
            all_transaction_objects = []

            for tryte in transaction_trytes['trytes']:
                transaction_inst = Transaction.from_tryte_string(tryte)

                all_transaction_objects.append(transaction_inst.as_json_compatible())

            return jsonify({
                'type': 'address',
                'payload': all_transaction_objects
            })

        return jsonify({
            'type': 'address',
            'payload': []
        })

    if len(search_string) == 81 and search_string.endswith('999'):

        # First looking for a result in database...
        transaction_result = lookup_api.fetch_transactions_by_hash(search_string)
        all_transaction_objects = []
        if transaction_result is not None:
            # return jsonify({
            #     'type': 'transaction',
            #     'payload': [res.get_transaction_data() for res in result]
            # })

            for res in transaction_result:
                all_transaction_objects.append(res.get_transaction_data())
        approvee_result = lookup_api.fetch_transaction_approvees(search_string)
            
        all_transaction_objects.append({
        "from": "transaction_result",
        "to": "approvee_result"
        })
        if approvee_result is not None:
            for res in approvee_result:
                all_transaction_objects.append(res.get_transaction_approvee_data())

        transaction_trytes, transaction_trytes_status_code = api.get_trytes([search_string])
        all_transaction_objects.append({
            "from": "cassandra",
            "to": "Full Node"
        })
        if transaction_trytes_status_code == 503 or transaction_trytes_status_code == 400:
            return jsonify({
                'type': 'transaction',
                'payload': all_transaction_objects
            })
            # abort(transaction_trytes_status_code)

        elif transaction_trytes_status_code == 200:
            if not transaction_trytes['trytes']:
                return jsonify({
                    'type': 'transaction',
                    'payload': []
                })
            for tryte in transaction_trytes['trytes']:
                transaction_inst = Transaction.from_tryte_string(tryte)
                all_transaction_objects.append(transaction_inst.as_json_compatible())

            return jsonify({
                'type': 'transaction',
                'payload': all_transaction_objects
            })

        return jsonify({
            'type': 'transaction',
            'payload': []
        })

    if len(search_string) == 81 and not search_string.endswith('999'):
        result = lookup_api.fetch_transactions_by_bundleHash(search_string)
        all_transaction_objects = []
        if result is not None:
            for res in result:
                all_transaction_objects.append(res.get_bundle_data())
        
        bundles, bundles_status_code = api.find_transactions(bundles=[search_string])
        if bundles_status_code == 503 or bundles_status_code == 400:
            abort(bundles_status_code)
        elif bundles_status_code == 200:
            if not bundles['hashes']:
                return jsonify({
                    'type': 'bundle',
                    'payload': all_transaction_objects
                })

            transaction_trytes, transaction_trytes_status_code = api.get_trytes(bundles['hashes'])

            bundle_inst = Bundle.from_tryte_strings(transaction_trytes['trytes'])
            all_transaction_objects.append(bundle_inst.as_json_compatible())

            return jsonify({
                'type': 'bundle',
                'payload': all_transaction_objects
            })

        return jsonify({
            'type': 'bundle',
            'payload': []
        })

    abort(404)
