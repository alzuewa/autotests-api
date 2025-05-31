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

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()


access_token = login_response_data['token']['accessToken']
user_id = create_user_response_data['user']['id']
patch_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

patch_user_headers = {'Authorization': f'Bearer {access_token}'}
httpx.patch(f'http://127.0.0.1:8000/api/v1/users/{user_id}', json=patch_user_payload, headers=patch_user_headers)
