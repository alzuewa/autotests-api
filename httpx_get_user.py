import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post('http://127.0.0.1:8000/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f'Create user response: {create_user_response_data}')
print(f'Create user status code: {create_user_response.status_code}', end='\n====\n')

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Login response: {login_response_data}')
print(f'Login status code: {login_response.status_code}', end='\n====\n')

access_token = login_response_data['token']['accessToken']
user_id = create_user_response_data['user']['id']

get_user_headers = {'Authorization': f'Bearer {access_token}'}
get_user_response = httpx.get(f'http://127.0.0.1:8000/api/v1/users/{user_id}', headers=get_user_headers)
get_user_response_data = get_user_response.json()

print(f'Get user response: {get_user_response_data}')
print(f'Get user status code: {get_user_response.status_code}', end='\n====\n')
