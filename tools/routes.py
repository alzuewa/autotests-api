from enum import StrEnum


class APIRoutes(StrEnum):
    AUTHENTICATION = '/api/v1/authentication'
    COURSES = '/api/v1/courses'
    EXERCISES = '/api/v1/exercises'
    FILES = '/api/v1/files'
    USERS = '/api/v1/users'
