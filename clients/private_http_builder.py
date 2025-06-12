from functools import lru_cache

from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings


# frozen is used for correct @lru_cache work
class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Function which creates httpx.Client instance with authentication.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use httpx.Client object with filled in Authorization header.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    response = authentication_client.login(login_request)
    access_token = response.token.access_token

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={'Authorization': f'Bearer {access_token}'},
        event_hooks={
            'request': [curl_event_hook, log_request_event_hook],
            'response': [log_response_event_hook]
        }
    )
