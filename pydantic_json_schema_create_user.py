from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password='string',
    last_name='string',
    first_name='string',
    middle_name='string'
)

# actual result
create_user_response = public_users_client.create_user_api(request=create_user_request)

# expected result
create_user_response_schema = CreateUserResponseSchema.model_json_schema(by_alias=True)

# compare actual and expected results
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)
