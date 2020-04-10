# 3.2.5
################


def read_file(file_name):
    """Try to open a file using exceptions """

    opening_string = "__CONTENT_START__\n"
    closing_string = "__CONTENT_END__\n"
    no_file_string = "__NO_SUCH_FILE__\n"
    try:
        file_id = open(file_name, 'r')
    except FileNotFoundError:
        string = opening_string + no_file_string
    else:
        string = opening_string + file_id.read()
    finally:
        # file_id.close()
        return string + closing_string


if __name__ == "__main__":
    file_exist = r"/home/liron/PycharmProjects/nextpy/one_lined_file.txt"
    file_does_not_exist = r"/home/liron/PycharmProjects/nextpy/file_does_not_exist.txt"
    print(read_file(file_exist))
    print(read_file(file_does_not_exist))
