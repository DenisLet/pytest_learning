import pytest

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
def test_something(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)
