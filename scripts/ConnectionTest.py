""" simply iterates through each item link to check and see if that page is available """

import json
import time

from urllib.request import urlopen

def main():

    link = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="

    f = open('res/items.json')
    json_string = f.read()
    item_dictionary = json.loads(json_string)

    item_ids = []
    counter = 0

    for item in item_dictionary:
        try:
            print("Checking item ID: " + str(item['id']))
            urlopen(link + str(item['id']))
            counter = counter + 1
            item_ids.append(item['id'])
            time.sleep(5) # sure I guess...
        except Exception as e:
            print(item['id']+ ": failed.")

    w = open('results.txt')

    for item in item_ids:
        w.write(item + '\n')

    print(counter)


main()
