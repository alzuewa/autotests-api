import allure
from allure_commons.types import AttachmentType
from httpx import Request, Response

from tools.formatters.curl import make_curl_from_request
from tools.logger import get_logger

# Initialize logger in global scope to avoid logging duplication
logger = get_logger('HTTP_LOGGER')


def curl_event_hook(request: Request):
    """
    Event hook to automatically append request in cURL format to Allure report
    :param request: HTTP-request passed to `httpx` client
    """
    curl_command = make_curl_from_request(request)

    allure.attach(body=curl_command, name='cURL command', attachment_type=AttachmentType.TEXT)


def log_request_event_hook(request: Request):
    """
    Logs info about sent HTTP-request
    :param request: HTTPX request object
    """
    logger.info(f'Send {request.method} request to {request.url}')


def log_response_event_hook(response: Response):
    """
    Logs info about received HTTP-response
    :param response: HTTPX response object
    """
    logger.info(f'Got response: {response.status_code}, reason: {response.reason_phrase} from {response.url}')
