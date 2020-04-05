# 1.3.4
################


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
"""Decode the password """
increased_letter = ''.join(list(map(lambda letter: chr(ord(letter) + 2) if letter.isalpha() else ' ', password)))

if __name__ == "__main__":
    print(increased_letter)
