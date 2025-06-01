from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema


public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(request=create_user_request)
print(f'Greate user data: {create_user_response}')

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user(user_id=create_user_response.user.id)
print(f'Get user data: {get_user_response}')
