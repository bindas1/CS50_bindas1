from cs50 import get_string
from sys import argv
from sys import exit

def main():
    if len(argv) != 2:
        print("Usage: python bleep.py banned.txt")
        exit(1)
    with open(argv[1]) as file:
        banned = file.readlines()
        stripped_banned = [s.rstrip() for s in banned]
        mes = get_string("What message would you like to censor?\n")
        mes_final = ""
        words = mes.split(" ")
        print(words)
        for word in words:
            if word.lower() in stripped_banned:
                for letter in word:
                    #hashing word
                    mes_final += "*"
                #space
                mes_final += " "
            else:
                # word not banned
                mes_final = mes_final + word + " "
        print(mes_final)

if __name__ == "__main__":
    main()
