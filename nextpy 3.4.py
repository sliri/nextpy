# 3.4
################
# import string library function
import string


class UsernameContainsIllegalCharacter(Exception):
    """A username validity exception class."""

    def __init__(self, username):
        """Initialize the username."""
        self.username = username

    def invalid_chars(self):
        """ Get a string, return the invalid set of chars in it as string.
        :type
        """
        bad_char = str()
        for char in self.username:
            if char.isalpha() or char.isdigit() or char == '_':
                continue
            else:
                bad_char = char
                break
        return [''.join(bad_char), self.username.index(bad_char)]

    def __str__(self):
        """The class description string"""
        return "The username contains an illegal character \"""%s\" at index %s" %(self.invalid_chars()[0] ,self.invalid_chars()[1])


class UsernameTooShort(Exception):
    """A user name length exception class."""

    def __init__(self, username):
        """Initialize the username."""
        self.username = username

    def __str__(self):
        """The class description string"""
        return "The username is too short. You used only %s chars minimum is 3." % len(self.username)


class UsernameTooLong(Exception):
    """A username length exception class."""

    def __init__(self, username):
        """Initialize the username."""
        self.username = username

    def __str__(self):
        """The class description string"""
        return "The username is too long. You used %s chars maximum is 16." % len(self.username)


class PasswordMissingCharacter(Exception):
    """A password validity exception class."""

    def __init__(self, password):
        """Initialize the password."""
        self.password = password

    def __str__(self):
        """The class description string"""
        return "The password is missing a character"


class PasswordMissingCharacterLower(PasswordMissingCharacter):
    """A password validity exception class."""

    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        """The class description string"""
        return PasswordMissingCharacter.__str__(self) + ' ' + '(Lower)'


class PasswordMissingCharacterUpper(PasswordMissingCharacter):
    """A password validity exception class."""

    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        """The class description string"""
        return PasswordMissingCharacter.__str__(self) + ' ' + '(Upper)'


class PasswordMissingCharacterDigit(PasswordMissingCharacter):
    """A password validity exception class."""

    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        """The class description string"""
        return PasswordMissingCharacter.__str__(self) + ' ' + '(Digit)'


class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    """A password validity exception class."""

    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        """The class description string"""
        return PasswordMissingCharacter.__str__(self) + ' ' + '(Special)'


class PasswordTooShort(Exception):
    """A password length exception class."""

    def __init__(self, password):
        """Initialize the username."""
        self.password = password

    def __str__(self):
        """The class description string"""
        return "The password is too short. You used only %s chars minimum is 8." % len(self.password)


class PasswordTooLong(Exception):
    """A password length exception class."""

    def __init__(self, password):
        """Initialize the username."""
        self.password = password

    def __str__(self):
        """The class description string"""
        return "The password is too long. You used %s chars maximum is 40." % len(self.password)


def check_input(username, password):
    try:
        if [char for char in username if not(char.isalpha() or char.isdigit() or char == '_')]:
            raise UsernameContainsIllegalCharacter(username)
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif not ''.join([char for char in password if char.islower()]):
            raise PasswordMissingCharacterLower(password)
        elif not ''.join([char for char in password if char.isupper()]):
            raise PasswordMissingCharacterUpper(password)
        elif not ''.join([char for char in password if char.isdigit()]):
            raise PasswordMissingCharacterDigit(password)
        elif not ''.join([char for char in password if char in string.punctuation]):
            raise PasswordMissingCharacterSpecial(password)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)

    except UsernameContainsIllegalCharacter as e:
        print(UsernameContainsIllegalCharacter(username))
    except UsernameTooShort as e:
        print(UsernameTooShort(username))
    except UsernameTooLong as e:
        print(UsernameTooLong(username))
    except PasswordMissingCharacterLower as e:
        print(PasswordMissingCharacterLower(password))
    except PasswordMissingCharacterUpper as e:
        print(PasswordMissingCharacterUpper(password))
    except PasswordMissingCharacterDigit as e:
        print(PasswordMissingCharacterDigit(password))
    except PasswordMissingCharacterSpecial as e:
        print(PasswordMissingCharacterSpecial(password))
    except PasswordTooShort as e:
        print(PasswordTooShort(password))
    except PasswordTooLong as e:
        print(PasswordTooLong(password))
    else:
        print('OK')


if __name__ == "__main__":
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")

