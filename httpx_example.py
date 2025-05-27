import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())

data = {
    'title': 'New task',
    'completed': False,
    'user_id': 1
}
response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
print(response.status_code)
print(response.request.headers)
print(response.json())

data = {'username': 'testuser', 'password': 12345}
response = httpx.post('https://httpbin.org/post', data=data)
print(response.status_code)
print(response.request.headers)
print(response.json())

headers = {'Authorization': 'Bearer my_secret_token'}
response = httpx.get('https://httpbin.org/get', headers=headers)
print(response.request.headers)
print(response.json())

params = {'userId': 1}
response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response.request)
print(response.json())

files = {'file': ('example.doc', open('example.txt', 'rb'))}
response = httpx.post('https://httpbin.org/post', files=files)
print(response.request.headers)
print(response.request.stream)
print(response.json())

with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
print(response1.json())
print(response2.json())

with httpx.Client(headers={'Authorization': 'Bearer my_secret_token'}) as client:
    response = client.get('https://httpbin.org/get')
print(response.json())

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid-url')
    print(
        response.status_code)  # 404 will be printed even though an Exception occurs here and it is intercepted by `except` block
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Request error: {e}')

try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout as e:
    print('Request exceeded timeout limit')
