# 3.2.5
################


class UnderAge(Exception):
    """An under age exception class"""

    def __init__(self, age):
        """Initialize the age"""
        self.age = age

    def __str__(self):
        """The class description string"""
        return "Your age is {}, wait another {} years so you can come to" \
               "Ido's birthday!".format(self.age, (18 - self.age))


def send_invitation(name, age):
    """Send invitation to a person if he/she is under 18"""
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print('Function expected a positive integer under 18 and got %s' % age)
    else:
        print("You should send an invite to " + name)


if __name__ == "__main__":
    send_invitation('Tali', 20)
    send_invitation('Tali', 17)
