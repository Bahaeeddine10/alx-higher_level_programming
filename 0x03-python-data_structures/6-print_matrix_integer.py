#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for xmatrix in matrix:
        if len(xmatrix) == 0:
            print()
        for i in range(len(xmatrix)):
            print("{:d}".format(xmatrix[i]), 
                    end="\n" if i is len(xmatrix) - 1 else " ")
