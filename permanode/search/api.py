from flask import jsonify, abort
from permanode.search import search
from permanode.search.helpers import Search
from config import Logger
from datetime import  datetime


@search.route('/<search_string>', methods=['GET'])
def fetch_associated_info(search_string):
    starting_time = datetime.now()
    if not search_string or len(search_string) > 90:
        Logger.logger.error("search string greater than 90",extra={"user_input": search_string,"response_time":datetime.now()-starting_time})
        abort(400)

    search_inst = Search(search_string)

    if len(search_string) <= 27:
        payload = search_inst.get_txs_for_tag()

        if payload is None:
            Logger.logger.error('Tag search error',extra={"user_input": search_string,"search type":"TAG","response_time":datetime.now()-starting_time})
            abort(404)
        
        Logger.logger.info('Tag search successfull',extra={"user_input": search_string,"search type":"TAG","response_time":datetime.now()-starting_time})
        return jsonify(payload)

    if len(search_string) == 90:
        payload = search_inst.get_txs_for_address()

        if payload is None:
            Logger.logger.error('Address with checksum error',extra={"user_input": search_string,"search type":"ADDRESS","response_time":datetime.now()-starting_time})
            abort(404)

        Logger.logger.info('Address with checksum successfull',extra={"user_input": search_string,"search type":"ADDRESS","response_time":datetime.now()-starting_time})
        return jsonify(payload)

    if len(search_string) == 81 and search_string.endswith('999'):
        
        payload = search_inst.get_txs()
        
        if payload is None:
            Logger.logger.error('Transaction search error',extra={"user_input": search_string,"search type":"TRANSACTION","response_time":datetime.now()-starting_time})
            abort(404)

        Logger.logger.info('Transaction search successfull',extra={"user_input": search_string,"search type":"TRANSACTION","response_time":datetime.now()-starting_time})
        return jsonify(payload)

    if len(search_string) == 81 and not search_string.endswith('999'):
        payload = search_inst.get_txs_for_bundle_hash_or_address()

        if payload is None:
            Logger.logger.error('Bundle Hash search error',extra={"user_input": search_string,"search type":"BUNDLE","response_time":datetime.now()-starting_time})
            abort(404)

        Logger.logger.info('Bundle Hash successfull',extra={"user_input": search_string,"search type":"BUNDLE","response_time":datetime.now()-starting_time})
        return jsonify(payload)
    Logger.logger.error('Nothing found',extra={"user_input": search_string,"search type":"NOT_DEFINED","response_time":datetime.now()-starting_time})
    abort(404)
