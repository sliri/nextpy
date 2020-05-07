# 5.4
################


class Error(Exception):
    """base class"""
    pass


class IdLengthError(Error):
    def __init__(self, id_number):
        print('Invalid  Length! your length is %s, required is 9' % len(str(id_number)))


class IdIterator():
    def __init__(self, _Id=000000000, _counter=0):
        self._Id = _Id
        self._counter = _counter

    def __iter__(self):
        return self

    def check_id_valid(self):
        if len(str(self._Id)) != 9:
            raise IdLengthError(self._Id)
        else:
            digit_list = list(int(x) for x in list(str(self._Id)))
            first_stage_list = [2 * digit if index % 2 else digit for index, digit in enumerate(digit_list)]
            second_stage_list = [number // 10 + number % 10 if number > 9 else number for number in first_stage_list]
            if sum(second_stage_list) % 10 == 0:
                return True
            else:
                return False

    def __next__(self):
        if self._Id > 999999999:
            raise StopIteration()
        elif self._counter > 9:
            raise StopIteration()
        if self.check_id_valid():
            self._counter += 1
            self._Id += 1
            return self._Id - 1
        else:
            self._Id += 1
            return None


def check_id_valid(id_number):
    if len(str(id_number)) != 9:
        raise IdLengthError(id_number)
    else:
        digit_list = list(int(x) for x in list(str(id_number)))
        first_stage_list = [2 * digit if index % 2 else digit for index, digit in enumerate(digit_list)]
        second_stage_list = [number // 10 + number % 10 if number > 9 else number for number in first_stage_list]
        if sum(second_stage_list) % 10 == 0:
            return True
        else:
            return False


def id_generator(id_number):
    counter = 1
    while True:
        if id_number > 999999999:
            raise StopIteration()
        elif counter > 10:
            break
        if check_id_valid(id_number):
            id_number += 1
            yield id_number - 1
            counter += 1
        else:
            id_number += 1


if __name__ == "__main__":
    IdIterator = IdIterator(123456780)
    for id in IdIterator:
        if id is None:
            pass
        else:
            print(id)
    print('\n')

    id_generator = id_generator(123456780)
    for id in id_generator:
        print(id)
