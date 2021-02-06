dict1 = {"name": "pongharit", "age": "20"}
dict2 = {"name": "pongharit", "age": "20"}
dict3 = dict1

print(dict1 is dict3)  # True

print(dict1 is dict2)  # False

print(dict1 == dict2)  # True