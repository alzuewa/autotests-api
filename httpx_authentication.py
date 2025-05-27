import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)

login_response_data = login_response.json()
print(f'Login response: {login_response_data}')
print(f'Login status code: {login_response.status_code}')

refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken']
}
refresh_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print(f'Refresh response: {refresh_response_data}')
print(f'Refresh status code: {refresh_response.status_code}')
