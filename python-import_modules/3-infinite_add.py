#!/usr/bin/python3
if __name__ == "__main__":
    # import the argv list from the sys module
    from sys import argv
    add = 0
    len = len(argv)
    if (len - 1 == 0):
        print('0')
    elif (len - 1 == 1):
        print(argv[1])
    else:
        for i in range(1, len):
            add += int(argv[i])
        print(add)
