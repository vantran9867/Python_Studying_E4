import json


def open_json_file(path):
    with open(path) as file:
        data = json.load(file)
    return data
