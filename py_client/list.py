import requests
from getpass import getpass

username = input('Enter your username:')
password = getpass('Enter your password:')

auth_endpoint = 'http://localhost:8000/api/auth/'
auth_response = requests.post(auth_endpoint, json={'username': username, 'password':password}) # HTTP Request
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }

    endpoint = 'http://localhost:8000/product/'
    get_response = requests.get(endpoint, headers=headers) # HTTP Request
    print(get_response.json())
    # print(get_response.json()[0]['title'])
    data = get_response.json()
    next_url = data['next']
    print('next_url:',next_url)
    results = data['results']
    print(results)
