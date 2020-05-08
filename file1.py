# 6.2.1
################


class GreetingCard():
    def __init__(self, _recipient='Dana Ev', _sender='Eyal Ch'):
        self._recipient = _recipient
        self._sender = _sender

    def greeting_msg(self):
        print("recipient is {}" .format(self._recipient))
        print("sender is {}" .format(self._sender))
