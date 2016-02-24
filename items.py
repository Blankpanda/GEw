""" maintains item list to match IDS to Names """
import json

class Items(object):

    def __init__(self, item_path):
        self.item_path = item_path
        self.items = self.read_json_file(item_path)
    
    # Returns Json read JSON string from a file as a dict.
    def read_json_file(self, fname):
        
        json_file = open(fname)
        json_string = json_file.read()
        
        return json.loads(json_string)

    # Simply reads JSON data that is already read in the program and returns a dict.
    def read_json(self, json_data):
        return json.loads(json_data)
