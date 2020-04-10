# 3.1.3
################


def StopIteration_error(test_list):
    i = 0
    while i > -4:
        print(test_list[i])
        i += 1


def ZeroDivision_Error():
    print(5 / 0)


def Assertion_Error(x):
    assert x == "hello"


def Import_Error():
    import functoolsy


def Key_Error():
    dictionary = {'name1': 'Dana', 'name2': 'kelly'}
    var = dictionary['name3']

# def Syntax_Error()
#     print('hello')
#
# def Indentation_Error():
# print('hello')

def TypeError():
    a = 5
    print(a+'e')

if __name__ == "__main__":
    StopIteration_error([1, 2, 3])
    # ZeroDivision_Error()
    # Assertion_Error("hellooo")
    #Import_Error()
    #Key_Error()
    #Syntax_Error()
    #Indentation_Error()
    # TypeError()
