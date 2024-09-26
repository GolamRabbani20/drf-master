import requests

headers = {'Authorization': 'Bearer 0ac50eb694d284447272091db53e81e15f04991e'}
endpoint = 'http://localhost:8000/product/'
data = {
    'title': 'Jackfruit',
    'price': 654
}
get_response = requests.post(endpoint, json=data, headers=headers) # HTTP Request
print(get_response.json())
