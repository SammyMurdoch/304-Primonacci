from sympy import nextprime
from math import sqrt
import numpy as np


def matrix_power_modulus(a, n, m):
    binary_digit_list = [int(d) for d in str(bin(n))[2:]]

    current_power = a
    matrix_powers = [current_power]

    for i in range(len(binary_digit_list) - 1):
        current_power = np.linalg.matrix_power(current_power, 2) % m

        matrix_powers.append(current_power)

    matrix_product = np.identity(2)

    for i, matrix in matrix_powers:
        if binary_digit_list[i] == 1:
            matrix_product = np.matmul(matrix_product, matrix) % m

    return matrix_product


def fibonacci_mod_m(n, m):
    return np.matmul(matrix_power_modulus(np.array([[0, 1], [1, 1]]), n, m), np.array([[0], [1]]))[0]


for i in range(10):
    print(fibonacci_mod_m(i, 100))


#print(matrix_power_modulus(np.array([[0, 1], [1, 1]]), 2, 1234567891011))

