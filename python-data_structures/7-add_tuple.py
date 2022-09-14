#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

# The below code also works
#    if (len(tuple_a) < 2):
#        if (len(tuple_a) == 0):
#            tuple_a = (0, 0)
#        else:
#            tuple_a = (tuple_a[0], 0)
#    if (len(tuple_b) < 2):
#        if (len(tuple_b) == 0):
#            tuple_b = (0, 0)
#        else:
#            tuple_b = (tuple_b[0], 0)
#
#    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

# Another method
#   a = len(tuple_a)
#   b = len(tuple_b)
#
#   sum = ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if a > 0 else 0),
#          (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if a > 1 else 0))

#   return sum
