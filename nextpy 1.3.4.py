# 1.3.4
################


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
"""Decode the password """
increased_letter = ''.join(list(map(lambda letter: chr(ord('a')+(ord(letter) + 2 - ord('a')) % 26).lower() if letter.isalpha() else ' ', password)))

if __name__ == "__main__":
    print(increased_letter)
