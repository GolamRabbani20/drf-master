import requests

headers = {'Authorization': 'Bearer cdf2fc59c055efda9099d766410c4266eff82ac4'} #Staff
endpoint = 'http://localhost:8000/api/product/'
data = {
    'title': 'Orange20',
    'price': 654
}
get_response = requests.post(endpoint, json=data, headers=headers) # HTTP Request
print(get_response.json())
