"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl, ValidationError, computed_field
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

    @computed_field
    def username(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_user_name(self) -> str:
        return  f'{self.first_name} {self.last_name}'


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = 'course-id'
    title: str = 'Playwright'
    max_score: int = Field(alias='maxScore', default=1000)
    min_score: int = Field(alias='minScore', default=10)
    preview_file: FileSchema = Field(alias='previewFile')
    description: str = 'Short description'
    estimated_time: str = Field(alias='estimatedTime', default='1 week')
    created_by_user: UserSchema = Field(alias='createdByUser')


course_standard_model = CourseSchema(
    id='course-id',
    title='Playwright',
    maxScore=100,
    minScore=10,
    previewFile=FileSchema(id='pr-id', filename='file-name', directory='courses', url='https://example.com/'),  # noqa
    description='course description',
    estimatedTime='2 weeks',
    createdByUser=UserSchema(id='123', email='user@example.com', lastName='Brown', firstName='Max', middleName='no')  # noqa
)
print(f'Course standard model: {course_standard_model}', type(course_standard_model))


course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
          "id": "pr-id",
          "filename": "file-name",
          "directory": "courses",
          "url": "https://example.com/"
        },
    "description": "course description",
    "estimatedTime": "2 weeks",
    "createdByUser": {
          "id": "123",
          "email": "user@example.com",
          "lastName": "Brown",
          "firstName": "Max",
          "middleName": "no"
        }
  }
course_dict_model = CourseSchema(**course_dict)
print(f'Course dict model: {course_dict_model}')


course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
          "id": "pr-id",
          "filename": "file-name",
          "directory": "courses",
          "url": "https://example.com/"
    },
    "description": "course description",
    "estimatedTime": "2 weeks",
    "createdByUser": {
          "id": "123",
          "email": "user@example.com",
          "lastName": "Brown",
          "firstName": "Max",
          "middleName": "no"
    }
}
"""
course_json = CourseSchema.model_validate_json(course_json)  # deserialization
print(f'Course json model: {course_json}')


print(course_json.model_dump(by_alias=True), type(course_json.model_dump()))
print(course_json.model_dump_json(by_alias=True), type(course_json.model_dump_json()))


course_default_model1 = CourseSchema(
    previewFile=FileSchema(id='pr-id', filename='file-name', directory='courses', url='https://example.com/'),  # noqa
    createdByUser=UserSchema(id='123', email='user@example.com', lastName='Brown', firstName='Max', middleName='no')  # noqa
)
print(f' Course default model: {course_default_model1}')

course_default_model2 = CourseSchema(
    maxScore=300,
    previewFile=FileSchema(id='pr-id', filename='file-name', directory='courses', url='https://example.com/'),  # noqa
    createdByUser=UserSchema(id='123', email='user@example.com', lastName='Brown', firstName='Max', middleName='no')  # noqa
)
print(f' Course default model: {course_default_model2}')


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = 'Playwright'
    max_score: int = Field(alias='maxScore', default=1000)
    min_score: int = Field(alias='minScore', default=10)
    preview_file: FileSchema = Field(alias='previewFile')
    description: str = 'Short description'
    estimated_time: str = Field(alias='estimatedTime', default='1 week')
    created_by_user: UserSchema = Field(alias='createdByUser')

try:
    course_1_id = CourseSchema()
    print(f' Course 1: {course_1_id}')

    course_2_id = CourseSchema()
    print(f' Course 2: {course_2_id}')

    course_3_id = CourseSchema(
        id='some-id',
        previewFile=FileSchema(id='pr-id', filename='file-name', directory='courses', url='https://example.com/'),  # noqa
        createdByUser=UserSchema(id='123', email='user@example.com', lastName='Brown', firstName='Max', middleName='no')  # noqa
    )
    print(f' Course 3: {course_3_id}')
except ValidationError as error:
    print(error)
    print(error.errors())  # getting a list of errors


user = UserSchema(id='123', email='user@example.com', lastName='Brown', firstName='Max', middleName='no')  # noqa
print(f'USER: {user.get_user_name()}', user.username)
