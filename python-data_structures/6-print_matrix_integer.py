#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print ("{:d}".format(num), end=" ")
        print()

print_matrix_integer(matrix)
