import math
import sys

sys.setrecursionlimit(15000)

def prime_factors(n):

    list_of_prime_factors = []
    while n % 2 == 0:
        list_of_prime_factors.append(2),
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            list_of_prime_factors.append(i),
            n = n / i

    if n > 2:
        list_of_prime_factors.append(n),

    return list_of_prime_factors


def is_perfect_root(n, exponent):

    factors = prime_factors(n)

    if len(factors) < exponent:
        return False

    if len(factors) % exponent != 0:
        return False

    current_factor = factors[0]

    for i in range(len(factors)):

        if factors[i] != current_factor:
            if i % exponent != 0:
                return False
            else:
                current_factor = factors[i]

    return True

def list_sum_zero(list, number):
    zero_list = []
    for i in range(number):
        zero_list.append(0)

    if list == zero_list:
        return True
    else:
        return False


file = open(r"/Users/kadripoldmaa/Desktop/python_logs/5_5.txt", "w")

def combination_finder(list, number_of_components, range_of_numbers, power, n):

    # if list components are 1 1 1 then print done
    if list_sum_zero(list, number_of_components):
        file = open(r"/Users/kadripoldmaa/Desktop/python_logs/5_5.txt", "a")
        file.write("cycle completed!!")
        return
    

    if len(list) == number_of_components:

        exponential_number = 0
        for l in range(number_of_components):
            exponential_number += list[l]**power


        if is_perfect_root(exponential_number, power):

            if list[1] != 0:
                file = open(r"/Users/kadripoldmaa/Desktop/python_logs/5_5.txt", "a")
                example_string = str(power)
                for j in range(number_of_components):
                    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
                    file.write(str(list[j]) + example_string.translate(SUP))
                    if j + 1 != number_of_components:
                        file.write(" + ")
                file.write(" = " + str(round(exponential_number**(1/power))) + example_string.translate(SUP) + ' is a solution \n')
                return


        else:
            return

    elif n <= range_of_numbers:
        a = n + 1
        combination_finder(list, number_of_components, range_of_numbers, power, a)
        if len(list) == 0:
            combination_finder(list + [n], number_of_components, range_of_numbers, power, 0)
        elif n <= list[len(list) - 1]:
            combination_finder(list + [n], number_of_components, range_of_numbers, power, 0)
    return


combination_finder([], 5, 40, 5, 0)
