#!/usr/bin/python3
def uppercase(str):
    new = ''
    for i in str:
        j = ord(i) - 32
        if 97 <= ord(i) <= 122:
            new = new + chr(j)
        else:
            new = new + i
    print("{}".format(new))
