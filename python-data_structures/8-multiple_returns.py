#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if sentence else None)

# The code below also works
#   if not sentence:
#       return (0, None)
#   return (len(sentence), sentence[0])
