import requests

endpoint = 'http://localhost:8000/api/product/2215588/'
get_response = requests.get(endpoint) # HTTP Request
print(get_response.json())
