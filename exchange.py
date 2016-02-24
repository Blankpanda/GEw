""" Handles API calls to Grand Exchange API.  essentially a wrapper """
from urllib.request import urlopen
import codecs
import json
import items

class Exchange(object):
    """ takes the ID of an item and gathers information from the Grand Exchange API """
    def __init__(self, item_id):


        # obtain item list 
        # link creation1 for accessing the api the api.
        self.api_link = self.create_api_link(item_id)        

        # call the API for the specific item
        self.item_json = self.download_data_from_url(self.api_link)
        self.item_json = self.item_json['item'] # returns the entire json object as a string. makes things easier

        # search for item from the API and populate the objects properties

        
        # properties returned from the api

        self.item = self.item_json
        self.icon = self.item_json['icon']
        self.icon_large = self.item_json['icon_large']
        self.id = self.item_json['id']
        self.type = self.item_json['type']
        self.typeIcon = self.item_json['typeIcon']
        self.name = self.item_json['name']
        self.description = self.item_json['description']
        self.members_item = self.item_json['members']
        self.price = self.item_json['current']['price']

        # market trends
        # item_json is segmented based off of the different outputs for trends
        current_json = self.item_json['current']
        today_json = self.item_json['today']
        three_month_json = self.item_json['day90']
        six_month_json = self.item_json['day180']
        

        # current trends
        self.current_trend = current_json['trend']
        self.current_price = current_json['price'] # remove ???

        # todays trends
        self.today_trend = today_json['trend']
        self.today_price = today_json['price'] # this is going to return how much the price has changed today

        # trends three months ago
        self.ThreeMonths_trend = three_month_json['trend']
        self.ThreeMonths_change = three_month_json['change']

        # trends six months ago
        self.SixMonth_trend = six_month_json['trend']
        self.SixMonth_change = three_month_json['change']
                

    # Returns Json read JSON string from a file as a dict.
    def read_json_file(self, fname):
        
        json_file = open(fname)
        json_string = json_file.read()
        
        return json.loads(json_string)

    # Simply reads JSON data that is already read in the program and returns a dict.
    def read_json(self, json_data):
        return json.loads(json_data)

    # self a complete link for an API call.
    def create_api_link(self, item_id):
        base_url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="
        return base_url + str(item_id)

        
    # Download JSON data from the API.
    def download_data_from_url(self, url):
        
        reader = codecs.getreader('utf-8') # just incase we need to define a reader to read the file
        response = urlopen(url) # downloads data from URL

        # read the downloaded data into a string
        json_data = json.load(reader(response))
        
        return json_data

    # used to retrieve an items id based off name
    @staticmethod
    def get_item_name_by_id(item_name):
        
        # used to match items to ID names
        item_info  = items.Items('res/items.json')
        item_list = item_info.items
        
        try:
            
            for i in range(0,len(item_list)):
                if item_list[i]['name'] == item_name:
                    return item_info['id']
                else:                
                    raise NameNotFoundExecption(item_name)

        except NameNotFoundExecption as e:
            print(e.value)
            

            
        
    # used to retrieve an items id based off its id
    @staticmethod
    def get_item_id_by_name(item_id):

        item_info = items.Items('res/items.json')
        item_list = item_info.items
        
        try:

            for i in range(0,len(item_list)):
                if item_list[i]['id']  == item_id:
                    return item_info['name']
                else:
                    raise IDOutOfRange(item_id)
                    
        except IDOutOfRange as e:
            print(e.value)
            

class IDOutOfRange(Exception):
    def __init__(self, value):
        self.value = "value was out of range of valid IDs"
    def __str__(self):
        return repr(self.value)
    
class NameNotFoundExecption(Exception):
    def __init__(self, value):
        self.value = "Name was not found."
    def __str__(self):
        return repr(self.value)
    