import requests

endpoint = 'http://localhost:8000/api/product/11/update/'


data = {
    'title': 'Amra',
    'price': 125
}
get_response = requests.put(endpoint, json=data) # HTTP Request
print(get_response.json())
