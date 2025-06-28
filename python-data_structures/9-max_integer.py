#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:  # If the list is empty
        return None

    max_val = my_list[0]  # Start by assuming the first element is the biggest

    for num in my_list:
        if num > max_val:
            max_val = num  # Update max_val if we find a bigger number

    return max_val
