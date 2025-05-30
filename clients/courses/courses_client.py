from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCoursesQuerySchema,
    UpdateCourseRequestSchema,
)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class CoursesClient(APIClient):
    """
    A client to work with /api/v1/courses.
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Method to get all courses for user with id `userId`.
        :param query: a dict with `userId`.
        :return: Response object of type httpx.Response.
        """
        return self.get('/api/v1/courses', params=query)  # noqa

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Method to create course.
        :param request: a dict with `title`, `maxScore`, `minScore`, `description`, `estimatedTime`,
        `previewFileId`, `createdByUserId`.
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/courses', json=request.model_dump(by_alias=True))

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def get_course_api(self, course_id: str) -> Response:
        """
        Method to get course by its id.
        :param course_id: id of the course.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Method to update course by its id.
        :param course_id: id of the course.
        :param request: a dict with `title`, `maxScore`, `minScore`, `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method to delete course by its id.
        :param course_id: id of the course.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/courses/{course_id}')


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Function which creates CoursesClient instance as HTTP-client with full setup.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use CoursesClient object.
    """
    client = get_private_http_client(user)
    return CoursesClient(client)
