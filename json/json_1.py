import json

# some JSON:
json_string = '{ "name": "Pongharit & Arm", "age":2,"city":"Thai"}'

# parse x:
python_dict = json.loads(json_string)

# the result is a Python dictionary:
print(python_ditc["name"])
print(python_ditc["age"])
print(python_ditc["city"])