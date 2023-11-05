#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = x2 = y1 = y2 = 0
    len_a = len(tuple_a) if len(tuple_a) <= 2 else 2
    len_b = len(tuple_b) if len(tuple_b) <= 2 else 2
    for i in range(len_a):
        if i == 0:
            x1 = tuple_a[i]
        else:
            y1 = tuple_a[i]
    for j in range(len_b):
        if j == 0:
            x2 = tuple_b[j]
        else:
            y2 = tuple_b[j]
    new_tuple = (x1 + x2, y1 + y2)
    return (new_tuple)
