import json


def get_operations(name):
    with open(name) as f:
       return json.load(f)

