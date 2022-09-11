#!/usr/bin/python3
def remove_char_at(str, n):
    return str[:n] + str[n + 1:]  if (n >= 0) else str

# The code below also works
#   if (n >= 0):
#       return str[:n] + str[n + 1:]
#   else:
#       return str
