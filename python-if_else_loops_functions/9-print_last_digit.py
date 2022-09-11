#!/usr/bin/python3
def print_last_digit(number):
    print(abs(number) % 10, end='')
    return(abs(number) % 10)

# The code below also works
#   last = abs(number) % 10
#   print("{}".format(last), end='') or print(f"{last}", end ='')
#   return last
