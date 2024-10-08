import requests

product_id = input('Enter product id that you want to delete?')
try:
    product_id = int(product_id)
except:
    print(product_id, 'is not a valid id!')
    product_id = None
    

if product_id:
    headers = {'Authorization': 'Bearer cdf2fc59c055efda9099d766410c4266eff82ac4'} # Staff
    endpoint = f'http://localhost:8000/api/product/{product_id}/delete/'
    get_response = requests.delete(endpoint, headers=headers) # HTTP Request
    print(get_response.status_code, get_response.status_code==204)