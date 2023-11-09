#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda new_matrix:list(map(lambda m: m**2, new_matrix)), matrix))
