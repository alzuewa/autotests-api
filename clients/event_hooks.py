import allure
from allure_commons.types import AttachmentType
from httpx import Request

from tools.formatters.curl import make_curl_from_request


def curl_event_hook(request: Request):
    curl_command = make_curl_from_request(request)

    allure.attach(body=curl_command, name='cURL command', attachment_type=AttachmentType.TEXT)