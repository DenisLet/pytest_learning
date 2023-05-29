from src.enums.user_enums import Status
from src.generators.player_local import PlayerLocalization

class Player:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status = Status.active.value):
        self.result['account_status'] = status
        return self

    def set_balancec(self, balance = 0 ):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar = 'https://www,soccer24.com'):
        self.result['avatar'] = avatar
        return self


    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balancec()
        self.result['localize'] = {
                'en': PlayerLocalization('en_US').build(),
                'ru': PlayerLocalization('ru_RU').build()
            }
        return self


    def update_inner_generator(self, key, generator):
        self.result[key] = generator.build()
        return self

    def build(self):
        return self.result


z = Player().set_balancec(20).set_status('fake').build()

print(z)