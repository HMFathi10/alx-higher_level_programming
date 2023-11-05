#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for i in range(len(tuple_a)):
        if i == 0:
            x1 = tuple_a[i]
        else:
            y1 = tuple_a[i]
    for j in range(len(tuple_b)):
        if j == 0:
            x2 = tuple_b[j]
        else:
            y2 = tuple_b[j]
    new_tuple = (x1 + x2, y1 + y2)
    return (new_tuple)
