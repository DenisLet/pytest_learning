from enum import Enum

class Genders(Enum):
    famle = 'female'
    male = 'male'

class Status(Enum):
    inactive = 'inactive'
    active = 'active'

class UserErrors(Enum):
    WORNG_EMAIL = 'email does not contain @'