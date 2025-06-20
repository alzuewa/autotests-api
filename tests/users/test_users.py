from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.suite(AllureFeature.USERS)
class TestUsers:

    @allure.title('Create user')
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.parametrize('email', ['mail.ru', 'gmail.com', 'example.com'])
    def test_create_user(
            self,
            email: str,
            public_users_client: PublicUsersClient
    ):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_users_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(response_data, request)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title('Get user me')
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(
            self,
            function_user: UserFixture,
            private_users_client: PrivateUsersClient
    ):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(get_user_response=response_data, create_user_response=function_user.response)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
