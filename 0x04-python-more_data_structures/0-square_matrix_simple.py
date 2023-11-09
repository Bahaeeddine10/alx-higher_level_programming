#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda newMat:list(map(lambda m: m**2, newMat)), matrix))
