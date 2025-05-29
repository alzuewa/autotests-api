from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class Course(TypedDict):
    """
    Course structure
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class GetCoursesQueryDict(TypedDict):
    """
    Request structure to get a courses list.
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Request structure to create course.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseDict(TypedDict):
    """
    Creation course response structure.
    """
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """
    Request structure to update course.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    A client to work with /api/v1/courses.
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Method to get all courses for user with id `userId`.
        :param query: a dict with `userId`.
        :return: Response object of type httpx.Response.
        """
        return self.get('/api/v1/courses', params=query)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Method to create course.
        :param request: a dict with `title`, `maxScore`, `minScore`, `description`, `estimatedTime`,
        `previewFileId`, `createdByUserId`.
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/courses', json=request)

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()

    def get_course_api(self, course_id: str) -> Response:
        """
        Method to get course by its id.
        :param course_id: id of the course.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Method to update course by its id.
        :param course_id: id of the course.
        :param request: a dict with `title`, `maxScore`, `minScore`, `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Method to delete course by its id.
        :param course_id: id of the course.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/courses/{course_id}')


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Function which creates CoursesClient instance as HTTP-client with full setup.
    :param user: AuthenticationUserSchema object with user email and password.
    :return: Ready-to-use CoursesClient object.
    """
    client = get_private_http_client(user)
    return CoursesClient(client)
