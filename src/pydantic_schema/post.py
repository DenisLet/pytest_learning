from pydantic import BaseModel, validator, ValidationError, Field

class Post(BaseModel):

    id: int = Field(le = 2)
    title: str
    # name: str = Field(alias = '_name')

    # @validator('id')
    # def check_id_is_less_2(cls, v):
    #     if v > 1:
    #         raise ValueError('Id is more then 2')
    #     else:
    #         return v






# {'id': 1, 'title': 'Post 1'}