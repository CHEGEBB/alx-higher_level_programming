#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            asciiNum = ord(str[i]) - 32
        else:
            asciiNum = ord(str[i])
        print("{}".format(chr(asciiNum)), end='')
    print()
