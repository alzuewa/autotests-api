import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']
headers = {'Authorization': f'Bearer {access_token}'}

client = httpx.Client(
    base_url='http://127.0.0.1:8000',
    timeout=30,
    headers=headers
)

get_user_me_response = client.get('/api/v1/users/me')
get_user_me_response_data = get_user_me_response.json()
print(get_user_me_response.text)
print(get_user_me_response_data)
