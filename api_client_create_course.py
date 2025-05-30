from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password='string',
    last_name='string',
    first_name='string',
    middle_name='string'
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename='image.jpg',
    directory='courses',
    upload_file='testdata/files/image.jpg'
)
create_file_response = files_client.create_file(create_file_request)
print(f'Create file data: {create_file_response}')

create_course_request = CreateCourseRequestSchema(
    title='My first course',
    max_score=20,
    min_score=2,
    description='Simple description',
    estimated_time='1 week',
    preview_file_id=str(create_file_response.file.id),
    created_by_user_id=str(create_user_response.user.id)
)
create_course_response = courses_client.create_course(create_course_request)
print(f'Create course data: {create_course_response}')
