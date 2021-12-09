from flask import Blueprint, request, jsonify
from flask_cors import CORS
from app.collectibles.collectibles_db import find_by_owner, insert_a_collectible, \
    find_by_item_id, delete_an_item, update_a_collectible, delete_an_item_by_object
from flasgger import Swagger, swag_from

# Var name of blueprint must match the prefex of this python file name
# This is so it can be used as an annotation
# After that we add _v1 to seperate versions of our API calls
collectibles_api_v1 = Blueprint(
    'collect_em_all_api_v1', 'collect_em_all_api_v1', url_prefix='/api/v1/')

CORS(collectibles_api_v1)

DEFAULT_ITEMS_PER_PAGE = 20

_response = {
    "response_body": "",
    "page": 0,
    "filters": {},
    "entries_per_page": 0,
    "total_results": 0,
}

@collectibles_api_v1.route('/item_id/<string:itemId>', methods=['GET'])
def api_get_item_by_id(itemId):
    """ Retrieve a specific item from a collection.
    ---
    tags:
      - Collection Item
    description:
        Retreive an item from a personal collection given a specific item id
    parameters:
      - name: itemId
        in: path
        type: string
        required: true
        description: Database Id of the individual item
    responses:
      200:
        description: Query Sucessfull
    """
    response_body , total_results = find_by_item_id(itemId)

    _response["response_body"] = response_body
    _response["total_results"] = total_results
    _response["page"] = 1;
    _response["entries_per_page"] = 1;

    return jsonify(_response)

@collectibles_api_v1.route('/collection/', methods=['GET'])
def api_collection_by_owner():
    """ A list of items in a persons collection.
    ---
    tags:
      - Collection
    description:
        Retreive items of a personal collection
    parameters:
      - name: Owner
        in: query
        type: string
        required: true
        default: "Ash"
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
    results_per_page = request.args.get("results_per_page")
    if results_per_page is None:
        results_per_page = DEFAULT_ITEMS_PER_PAGE

    response_body , total_results = find_by_owner(owner_id, int(results_per_page))

    _response["response_body"] = response_body
    _response["total_results"] = total_results
    _response["page"] = 1;
    _response["entries_per_page"] = results_per_page;

    return jsonify(_response)


@collectibles_api_v1.route('/item/', methods=['POST'])
def api_add_item():
    """ Add a new item to a collection
    ---
    tags:
      - Collection Item
    parameters:
      - name: item details
        in: body
        required: true
        schema:
          id: Item
          type: object
          required:
            - ownerId
            - itemName
          properties:
            ownerId:
              type: string
              description: The owner of an item
              default: "Ash"
            itemName:
              type: string
              description: Name of item.
            quantity:
              type: string
              description: How many of this item?
            __Other__:
              type: string
              description: Any other user defined attribute of the item
    responses:
      201:
        description: A list of items in your collection
    """
    data = request.json    
    insert_a_collectible(data)
    return data


@collectibles_api_v1.route('/item_id/<string:itemId>', methods=['DELETE'])
def api_delete_item(itemId):
    """ Delete a specific item from a collection.
    ---
    tags:
      - Collection Item
    description:
        Delete an item from a personal collection given a specific item id
    parameters:
      - name: itemId
        in: path
        type: string
        required: true
        description: Database Id of the individual item
    responses:
      200:
        description: Delete Sucessfull
    """
    response, _ = delete_an_item(itemId)
    return jsonify(response)


@collectibles_api_v1.route('/item/delete', methods=['DELETE'])
def api_delete_item_by_name():
    """ Delete a specific item from a collection.
    ---
    tags:
      - Collection Item
    parameters:
      - name: item details
        in: body
        required: true
        schema:
          id: Item Delete
          type: object
          required:
            - ownerId
            - itemName
          properties:
            ownerId:
              type: string
              description: The owner of an item
              default: "Ash"
            itemName:
              type: string
              description: Name of item.
    responses:
      200:
        description: Successful delete
    """
    data = request.json    
    delete_an_item_by_object(data)
    return data

@collectibles_api_v1.route('/item/<string:itemId>', methods=['PATCH'])
def api_update_item(itemId):
    """ Update an existing items in a collection
    ---
    tags:
      - Collection Item
    parameters:
      - name: itemId
        in: path
        type: string
        required: true
        description: Database Id of the individual item    
      - name: item details
        in: body
        required: true
        schema:
          id: Item
          type: object
          properties:
            owner_id:
              type: string
              description: The owner of an item                
            itemName:
              type: string
              description: Name of item.
            quantity:
              type: string
              description: How many of this item?              
            __any_field__:
              type: string
              description: Identify any field that needs updating
    responses:
      200:
        description: Updating an existing item
    """
    data = request.json    
    new_record, _ = update_a_collectible(itemId, data)
    return new_record