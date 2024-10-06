import requests
product_id = input('Enter product id to show detail:')
try:
    product_id = int(product_id)
except:
    product_id = None
    print('Product id is not valid!')
if product_id:
    headers = {'Authorization': 'Bearer cdf2fc59c055efda9099d766410c4266eff82ac4'} # Staff
    endpoint = f'http://localhost:8000/api/product/{product_id}/'
    get_response = requests.get(endpoint, headers=headers) # HTTP Request
    print(get_response.json())
