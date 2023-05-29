import pytest
import requests
from config import SERVICE_URL, SERVICE_URL1
from src.schemes.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schema.post import Post
from src.schemes.user import User



@pytest.mark.production
def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)
@pytest.mark.skip('[ISSUE-23415] issue with network connection')
def test_another():
    '''
    Try to check that 1 is equal 2

    '''
    assert 1 == 2



@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1,2,3),
    (-1,-2,-3),
    (-1,2,1),
    ('b', -2, None),
    ('b','b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    '''
    In test we are testing ......
    '''
    assert calculate(first_value, second_value) == result

def test_anotherone():
    assert 1 == 2
