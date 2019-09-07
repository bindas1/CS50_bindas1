import sys
from cs50 import get_string

if len(sys.argv) == 2:
    if sys.argv[1].isalpha():
        key = sys.argv[1]
        key_len = len(sys.argv[1])
        i = 0
        plain = get_string("plaintext: ")
        print("ciphertext: ", end="")
        for letter in plain:
            if not letter.isalpha():
                print(letter, end="")
                continue
            else:
                # setting key
                key_letter = key[i % key_len]
                if key_letter.isupper():
                    k = ord(key_letter) - 65
                else:
                    k = ord(key_letter) - 97
                i += 1
                if not letter.isupper():  # male literki
                    letter = chr(97 + (ord(letter)+k-97) % 26)
                    print(letter, end="")
                else:  # duze literki
                    letter = chr(65 + (ord(letter)+k-65) % 26)
                    print(letter, end="")
        print("")
    else:
        sys.exit(1)
else:
    print("inappropriate number of arguments!")
    sys.exit(1)