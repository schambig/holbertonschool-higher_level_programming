#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print("{:c}".format(i), end="")

# other way (not accepted by the checker)
# for i in range(97, 123):
#     print(chr(i), end="")
