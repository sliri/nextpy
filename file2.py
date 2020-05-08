# 6.2.1
################

import file1


class BirthdayCard(file1.GreetingCard):
    def __init__(self, _sender_age=0):
        file1.GreetingCard.__init__(self)
        self._sender_age = _sender_age

    def greeting_msg(self):
        file1.GreetingCard.greeting_msg(self)
        print("Happy Birthday! {}".format(self._sender)+" age is {}".format(self._sender_age))

