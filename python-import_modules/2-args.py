#!/usr/bin/python3

# this "guard" protects users from accidentally invoking the script
# when they didn't intend to.
if __name__ == "__main__":

    # import the argv list from the sys module (set of packages)
    from sys import argv

    len = len(argv)
    if (len - 1) == 1:
        print("1 argument:")
    else:
        print(f"{len - 1} arguments:" if (len - 1) else "0 arguments.")
    for i in range(1, len):
        print(f"{i}: {argv[i]}")
