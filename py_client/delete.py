import requests

product_id = input('Enter product id that you want to delete?')
try:
    product_id = int(product_id)
except:
    print(product_id, 'is not a valid id!')
    product_id = None
    

if product_id:
    endpoint = f'http://localhost:8000/product/{product_id}/delete/'
    get_response = requests.delete(endpoint) # HTTP Request
    print(get_response.status_code, get_response.status_code==204)