from flask import jsonify, abort
from permanode.search import search
from permanode.search.helpers import Search
from config import Logger


@search.route('/<search_string>', methods=['GET'])
def fetch_associated_info(search_string):
    if not search_string or len(search_string) > 90:
        Logger.logger.error("search string greater than 90")
        abort(400)

    search_inst = Search(search_string)

    if len(search_string) <= 27:
        payload = search_inst.get_txs_for_tag()

        if payload is None:
            Logger.logger.error(search_string)
            abort(404)
        
        Logger.logger.info('tag')
        return jsonify(payload)

    if len(search_string) == 90:
        payload = search_inst.get_txs_for_address()

        if payload is None:
            Logger.logger.error(search_string)
            abort(404)

        Logger.logger.info('address with checksum')
        return jsonify(payload)

    if len(search_string) == 81 and search_string.endswith('999'):
        
        payload = search_inst.get_txs()
        
        if payload is None:
            Logger.logger.error(search_string)
            abort(404)

        Logger.logger.info('Transection')
        return jsonify(payload)

    if len(search_string) == 81 and not search_string.endswith('999'):
        payload = search_inst.get_txs_for_bundle_hash_or_address()

        if payload is None:
            Logger.logger.error(search_string)
            abort(404)

        Logger.logger.info('Bundle hash')
        return jsonify(payload)
    Logger.logger.error(search_string)
    abort(404)
