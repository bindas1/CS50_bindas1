import sys
from cs50 import get_string

if len(sys.argv) == 2:
    k = int(sys.argv[1])
    plain = get_string("plaintext: ")
    #print("plaintext: ", end="")
    #plain = input()
    print("ciphertext: ", end="")
    for letter in plain:
        if not letter.isalpha():
            print(letter, end="")
            continue
        else:
            if not letter.isupper():  # male literki
                letter = chr(97 + (ord(letter)+k-97) % 26)
                print(letter, end="")
            else:  # duze literki
                letter = chr(65 + (ord(letter)+k-65) % 26)
                print(letter, end="")
    print("")
else:
    print("inappropriate number of arguments!")
    sys.exit(1)