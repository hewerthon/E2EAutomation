import json


odics = '{"k1":"val1","k2":"val2"}'
print(type(odics))
json_result = json.load(odics)

print(json_result['k1'])