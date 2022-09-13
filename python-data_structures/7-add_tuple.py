#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    if (len(tuple_a) < 2):
        if (len(tuple_a) == 0):
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if (len(tuple_b) < 2):
        if (len(tuple_b) == 0):
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    for i in range(0, 2):
        res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
