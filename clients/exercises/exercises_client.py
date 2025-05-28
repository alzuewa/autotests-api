from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Request structure to get an exercises list.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Request structure to create exercise.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Request structure to update exercise.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    A client to work with /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Method to get all exercises in course with id `courseId`.
        :param query: a dict with `courseId`.
        :return: Response object of type httpx.Response.
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to get exercise by its id.
        :param exercise_id: id of the exercise.
        :return: Response object of type httpx.Response.
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Method to create exercise.
        :param request: a dict with `title`, `courseId`, `maxScore`, `minScore`, `orderIndex`,
        `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Method to update exercise by its id.
        :param exercise_id: id of the exercise.
        :param request: a dict with `title`, `maxScore`, `minScore`, `orderIndex`, `description`, `estimatedTime`.
        :return: Response object of type httpx.Response.
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method to delete exercise by its id.
        :param exercise_id: id of the exercise.
        :return: Response object of type httpx.Response.
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')
