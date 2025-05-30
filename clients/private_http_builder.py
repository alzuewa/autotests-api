from httpx import Client
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    email: EmailStr
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Function which creates httpx.Client instance with authentication.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use httpx.Client object with filled in Authorization header.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=str(user.email), password=user.password)
    response = authentication_client.login(login_request)
    access_token = response.token.access_token

    return Client(
        timeout=100,
        base_url='http://127.0.0.1:8000',
        headers={'Authorization': f'Bearer {access_token}'}
    )
