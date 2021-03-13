  
import json

# a Python object (dict):
python_dict = {"name": "Pongharit & Arm", "age": 22, "city": "Thai"}

# convert into JSON:
json_string = json.dump(python_dict)

# the result is a JSON string:
print(json_string)