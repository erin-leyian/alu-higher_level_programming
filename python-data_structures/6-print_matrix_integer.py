#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range (len ( row)):
            if i < len (row)- 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()

if __name__ == "__main__":
    print_matrix_integer(matrix)
