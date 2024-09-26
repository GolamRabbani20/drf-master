import requests

# endpoint = 'https://httpbin.org/status/200'
# endpoint1 = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'  # http://127.0.0.1:8001/


get_response = requests.post(endpoint, json={'title': 'Apple' ,'content': 'OK', 'price': 120}) # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# print(dir(requests))
print(get_response.json())
# print(get_response.status_code)

# print("------------------------------------------")
# get_response1 =  requests.get(endpoint1, params={'id': 456}, json={'name': 'Rabbani'})
# print(get_response1.json())
