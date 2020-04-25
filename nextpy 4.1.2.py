# 4.1.2
################


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    spanish_generator = (word for word in sentence.split(' '))
    returned_str = str()
    for word in spanish_generator:
        returned_str += words[word]+' '
    return returned_str


if __name__ == "__main__":
    print(translate("el gato esta en la casa"))
