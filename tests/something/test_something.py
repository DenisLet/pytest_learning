import pytest
from src.generators.player_local import PlayerLocalization
@pytest.mark.parametrize('status',[
    'ACTIVE',
    'BANNED',
    'DELECED',
    'INACTIVE'
])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())



@pytest.mark.parametrize('delete_key',[
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_something1(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def something2(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator('localize', {PlayerLocalization('fr_FR')}).build()
    print(object_to_send)


