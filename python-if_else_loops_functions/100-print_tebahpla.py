#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format(i) if (i % 2 == 0) else "{:c}".format(i - 32), end='')

# The code below also works
#   print(f"{chr(i)}" if (i % 2 == 0) else f"{chr(i - 32)}", end='')
# This is another method
#   print(f"{chr(i) if (i % 2 == 0) else chr(i - 32)}", end='')
