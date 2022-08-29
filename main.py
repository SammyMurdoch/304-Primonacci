from sympy import nextprime
import numpy as np
import time


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
    return int(np.matmul(matrix_power_modulus(np.array([[0, 1], [1, 1]], dtype=object), n, mod), np.array([[0], [1]]))[1][0])


start_time = time.time()

# mod = 1234567891011
# prime = 10 ** 14
# max_n = 10 ** 5

mod = 10
prime = 0
max_n = 10

total = 0

for i in range(max_n):
    prime = nextprime(prime)

    total = (total + fibonacci_mod_m(prime-1, mod)) % mod

print(time.time()-start_time)

print(total)
