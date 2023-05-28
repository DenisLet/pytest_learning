from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Status, UserErrors

class User(BaseModel):
    id: int
    name: int
    email: str
    gender: Genders
    status: Status

    @validator('email')
    def check_dot_in_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WORNG_EMAIL.value)

