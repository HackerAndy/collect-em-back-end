from flask import Blueprint, request, jsonify
from flask_cors import CORS
from app.collectibles.collectibles_db import find_by_owner

# Var name of blueprint must match the prefex of this python file name
# This is so it can be used as an annotation
# After that we add _v1 to seperate versions of our API calls
collectibles_api_v1 = Blueprint(
    'collect_em_all_api_v1', 'collect_em_all_api_v1', url_prefix='/api/v1/collection')

CORS(collectibles_api_v1)

DEFAULT_ITEMS_PER_PAGE = 20

_response = {
    "response_body": "",
    "page": 0,
    "filters": {},
    "entries_per_page": 0,
    "total_results": 0,
}

@collectibles_api_v1.route('/', methods=['GET'])
def api_collection_by_owner():
    """ Endpoint returning a list of items in a persons collection.
    ---
    description:
        Retreive items of a personal collection
    parameters:
      - name: Owner
        in: query
        type: string
        required: true
        default: "Bob"
        description: The owner of a collection.
      - name: results_per_page
        in: query
        type: string
        required: true
        default: 20
        description: Number of records to be returned per page
    responses:
      200:
        description: A list of items in your collection
    """
    owner_id = request.args.get("Owner")
    results_per_page = int(request.args.get("results_per_page"))
    if results_per_page is None or results_per_page <=0:
        results_per_page = DEFAULT_ITEMS_PER_PAGE

    response_body , total_results = find_by_owner(owner_id, results_per_page)

    _response["response_body"] = response_body
    _response["total_results"] = total_results
    _response["page"] = 1;
    _response["entries_per_page"] = results_per_page;

    return jsonify(_response)


@collectibles_api_v1.route('/', methods=['GET'])
def api_collection_by_owner():