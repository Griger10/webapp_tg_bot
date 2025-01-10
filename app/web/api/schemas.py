import re

from pydantic import BaseModel, Field, EmailStr, field_validator


class CreateForm(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=1)
    email: EmailStr
    phone_number: str

    @classmethod
    @field_validator('phone_number', mode='before')
    def phone_number_validator(cls, value):
        if not re.fullmatch(r'^+7 (\d{3}) \d{3}-\d{2}-\d{2} $', value):
            raise ValueError('Incorrect phone number of format! Try again!')
        return value


