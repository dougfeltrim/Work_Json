#This program get and print in the screen all the fields name from a JSON file
import json
from pprint import pprint

json_data=open('your_file.json')
data = json.load(json_data)
#Print all content of fields called name.
for i in range (0, len (data['resources'])):
    print data['resources'][i]['name']

json_data.close()
