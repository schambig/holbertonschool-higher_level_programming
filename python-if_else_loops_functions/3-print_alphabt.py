#!/usr/bin/python3
# using ord('a') instead of the ascci code also works
for i in range(97, 123):
    # to use continue we have to use == instead of !=
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
