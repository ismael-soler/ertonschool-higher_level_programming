#!/usr/bin/pyton3
def uppercase(str):
    for i in str:
        charNum = ord(i)
        if (charNum >= 97 and charNum <= 122):
            charNum = charNum - 32
        print("{}".format(chr(charNum)), end="")
    print()
