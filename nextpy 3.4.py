# 3.4
################
# import string library function
import string


def invalid_chars(input_str):
    """ Get a string, return the invalid set of chars in it as string.
    :type input_str: str
    """
    returned_str = str()
    for char in input_str:
        if char.isalpha() or char.isdigit() or char == '_':
            pass
        else:
            returned_str += char
    return ''.join(set(returned_str))


def missing_chars(input_str):
    """ Get a string, find the missing set of chars in it as string.

    The string must contain one small letter, one capital letter, a number and a special char
    :type input_str: string
    """
    lower_string = ''.join([char for char in input_str if char.islower()])
    upper_string = ''.join([char for char in input_str if char.isupper()])
    digit_string = ''.join([char for char in input_str if char.isdigit()])
    special_string = ''.join([char for char in input_str if char in string.punctuation])
    lower_error = upper_error = digit_error = special_error = str()
    if not lower_string:
        lower_error = 'missing lower letter\n'
    if not upper_string:
        upper_error = 'missing upper letter\n'
    if not digit_string:
        digit_error = 'missing digit\n'
    if not special_string:
        special_error = 'missing special letter\n'
    return lower_error + upper_error + digit_error + special_error


class UsernameContainsIllegalCharacter(Exception):
    """A username validity exception class."""

    def __init__(self, username):
        """Initialize the username."""
        self.username = username

    def __str__(self):
        """The class description string"""
        return "Illegal chars in username! You used the chars %s. Only alphanumeric or '_' are allowed." % \
               (invalid_chars(self.username))


class UsernameTooShort(Exception):
    """A user name length exception class."""

    def __init__(self, username):
        """Initialize the username."""
        self.username = username

    def __str__(self):
        """The class description string"""
        return "username too short! You used only %s chars minimum is 3." % len(self.username)


class UsernameTooLong(Exception):
    """A username length exception class."""

    def __init__(self, username):
        """Initialize the username."""
        self.username = username

    def __str__(self):
        """The class description string"""
        return "username too long! You used %s chars maximum is 16." % len(self.username)


class PasswordMissingCharacter(Exception):
    """A password validity exception class."""

    def __init__(self, password):
        """Initialize the username."""
        self.password = password

    def __str__(self):
        """The class description string"""
        return "The password must contain one small letter, one capital letter" \
               " a number and punctuation.\n%s" % (missing_chars(self.password))


class PasswordTooShort(Exception):
    """A password length exception class."""

    def __init__(self, password):
        """Initialize the username."""
        self.password = password

    def __str__(self):
        """The class description string"""
        return "password too short! You used only %s chars minimum is 8." % len(self.password)


class PasswordTooLong(Exception):
    """A password length exception class."""

    def __init__(self, password):
        """Initialize the username."""
        self.password = password

    def __str__(self):
        """The class description string"""
        return "username too long! You used %s chars maximum is 40." % len(self.password)


def check_input(username, password):
    try:
        if invalid_chars(username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif missing_chars(password):
            raise PasswordMissingCharacter(password)
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
    except PasswordMissingCharacter as e:
        print(PasswordMissingCharacter(password))
    except PasswordTooShort as e:
        print(PasswordTooShort(password))
    except PasswordTooLong as e:
        print(PasswordTooLong(password))
    else:
        print('OK')


if __name__ == "__main__":
    check_input("usyuyit", 'rE&r1')

