""" read the item.json file in order to match names to IDs and vice versa """
import json
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_id(item_name):
    """ matches an item name to an id in items.json """
    path = os.path.join(_ROOT, 'items.json')
    items = read_json_file(path)

    for item_info in items:
        if item_name == item_info['name']:
            return item_info['id']
    return None

def get_name(item_id):
    """ matches an item id to a name in items.json """
    path = os.path.join(_ROOT, 'items.json')
    items = read_json_file(path)

    for item_info in items:
        if item_id == item_info['id']:
            return item_info['name']

    return None

def read_json_file(path):
    """ converts a json file to a dict """

    f = open(path)
    json_string = f.read()
    return json.loads(json_string)
