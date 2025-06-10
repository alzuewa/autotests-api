from typing import Any

import allure
from httpx import Client, QueryParams, Response, URL
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        Base API client taking httpx.Client.
        :param client: httpx.Client instance to perform HTTP-requests.
        """
        self.client = client

    @allure.step('Send GET request to {url}')
    def get(self, url: URL | str, *, params: QueryParams | None = None) -> Response:
        """
        Performs GET-request.

        :param url: endpoint URL-address.
        :param params: GET-request query params (for instance, ?key=value).
        :return: Response object of type httpx.Response.
        """
        return self.client.get(url, params=params)

    @allure.step('Send POST request to {url}')
    def post(
            self,
            url: URL | str,
            *,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Performs POST-request
        :param url: endpoint URL-address.
        :param json: JSON-formatted data.
        :param data: form-data (for instance, application/x-www-form-urlencoded)
        :param files: files to upload to the server
        :return: Response object of type httpx.Response.
        """
        return self.client.post(url, data=data, files=files, json=json)

    @allure.step('Send PATCH request to {url}')
    def patch(self, url: URL | str, *, json: Any | None = None) -> Response:
        """
        Performs PATCH-request
        :param url: endpoint URL-address.
        :param json: JSON-formatted data.
        :return: Response object of type httpx.Response.
        """
        return self.client.patch(url, json=json)

    @allure.step('Send DELETE request to {url}')
    def delete(self, url: URL | str) -> Response:
        """
        Performs DELETE-request
        :param url: endpoint URL-address.
        :return: Response object of type httpx.Response.
        """
        return self.client.delete(url)
