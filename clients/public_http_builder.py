from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:
    """
    Function which creates httpx.Client instance with base settings.
    :return: Ready-to-use httpx.Client object.
    """
    return Client(
        timeout=100,
        base_url='http://127.0.0.1:8000',
        event_hooks={'request': [curl_event_hook]}
    )