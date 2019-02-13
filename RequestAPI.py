import requests
import json
import jsonpath


api_url = 'https://reqres.in/api/users?page=2'

# Make a request

resp = requests.get(api_url)
print(resp.text)

# Validate Status code

assert resp.status_code == 200

# Parse response into JSON format

json_response = json.loads(resp.text)

print(json_response)

# Apply JSON Path
x = jsonpath.jsonpath(json_response, 'total')

print(x)

y = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(y)