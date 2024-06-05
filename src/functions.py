import json
from datetime import datetime


def get_operations(name):
    with open(name) as f:
        return json.load(f)


operations = get_operations('operations.json') #в мэйн


def sort_operations():
    datetime_objects = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in operations]
    print(datetime_objects.sort(reverse=True))






#date_list = []
#for element in operations:
#   if element.get('date') is not None and element.get('state') == "EXECUTED":
#      element['date'] = datetime.fromisoformat(element['date'])
#      date_list.append(element)
#return date_list
