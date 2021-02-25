import json

with open('aus_covid.json') as json_file:
    data = json.load(json_file)
    print(data[0])