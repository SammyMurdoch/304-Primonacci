from sympy import nextprime
from math import sqrt
import numpy as np


def generate_matrix_power_list(m, max_power, mod):
    current_power = m
    matrix_powers = [current_power]

    for i in range(max_power-1):
        current_power = np.linalg.matrix_power(current_power, 2) % mod

        matrix_powers.append(current_power)

    return matrix_powers


def matrix_power_modulus(m, power, mod):
    binary_digit_list = [int(d) for d in str(bin(power))[2:]]

    matrix_powers = generate_matrix_power_list(m, len(binary_digit_list), mod)

    matrix_product = np.identity(2)

    for i, matrix in enumerate(matrix_powers[::-1]):
        if binary_digit_list[i] == 1:
            matrix_product = np.matmul(matrix_product, matrix) % mod

    return matrix_product


def fibonacci_mod_m(n, mod):
    return np.matmul(matrix_power_modulus(np.array([[0, 1], [1, 1]]), n, mod), np.array([[0], [1]]))[1]

#
# for i in range(10):
#     print(fibonacci_mod_m(i, 10))


print(fibonacci_mod_m(10**14, 1234567891011))


#hi = np.array([[0, 1], [1, 1]])
#
#print(matrix_power_modulus(hi, 4, 2))
#
# print(np.matmul(hi, hi) % 2)

#print(generate_matrix_power_list(hi, 2, 2)[2])


