#This program get and print in the screen all the fields name from a JSON file
import json
from pprint import pprint

json_data=open('Insomnia.json')
data = json.load(json_data)

for i in range (0, len (data['resources'])):
    print data['resources'][i]['name']

json_data.close()
