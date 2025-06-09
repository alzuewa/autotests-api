from pydantic import BaseModel, ConfigDict, EmailStr, Field

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    User structure
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Request structure to create user.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """"
    Creation user response structure
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Request structure to update user.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str | None = Field(default_factory=fake.email)
    lastName: str | None = Field(alias='lastName', default_factory=fake.last_name)
    firstName: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middleName: str | None = Field(alias='middleName', default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """"
    Updating user response structure
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """"
    Getting user response structure
    """
    user: UserSchema
