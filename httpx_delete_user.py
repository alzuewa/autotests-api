import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
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

delete_user_headers = {'Authorization': f'Bearer {access_token}'}
delete_user_response = httpx.delete(f'http://127.0.0.1:8000/api/v1/users/{user_id}', headers=delete_user_headers)
print(f'Delete user status code: {delete_user_response.status_code}', end='\n====\n')
