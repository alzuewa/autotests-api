import httpx

from tools.fakers import get_random_email

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post('http://127.0.0.1:8000/api/v1/users', json=payload)
create_user_response_data = create_user_response.json()
print(f'Create user response: {create_user_response_data}')
print(f'Create user status code: {create_user_response.status_code}')
