#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0 or not idx):
        return my_list
    new_list = []
    for i in my_list:
        if (i == my_list[idx]):
            continue
        else:
            new_list.append(i)
    return new_list
