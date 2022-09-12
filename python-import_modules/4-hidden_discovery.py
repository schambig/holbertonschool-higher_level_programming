#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for line in (line for line in dir(hidden_4) if not line.startswith('__')):
        print(line)
