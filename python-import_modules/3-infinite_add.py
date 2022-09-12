#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    if (len(argv) > 1):
        for i in range(1, len(argv)):
            add += int(argv[i])
    print(add)  # or print(f"{add}"), or print("{:d}".format(add))

# The code below also works
#    add = 0
#    len = len(argv)
#    if (len - 1 == 0):
#        print('0')
#    elif (len - 1 == 1):
#        print(argv[1])
#    else:
#        for i in range(1, len):
#            add += int(argv[i])
#        print(add)
