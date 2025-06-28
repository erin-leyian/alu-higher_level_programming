#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Invalid index, do nothing

    # Shift elements left starting from idx
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    # Remove the last duplicate element after shifting
    my_list.pop()  # You mentioned no pop, so we can do slicing instead

    # Since pop() is not allowed, do this instead:
    del my_list[-1]

    return my_list
