import json
# jsonschema is an implementation of the JSON Schema specification for Python.
from jsonschema import validate
f = open("C:\\Users\\venuy\\Mylearning\\MyRepo\\data\\data_subset.json")
data = json.load(f)
print(data)
