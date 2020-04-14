'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
num = 600_851_475_143 #12 digits 600,851,475,143
test = 13_195

def is_prime(n):
    
    if n == 1: return False

    for i in range(2, 1 + math.floor(math.sqrt(n))):
        if n % i == 0: return False
    return True

def largest_prime_factor(l):
    factor = 0
    for i in range(2, math.floor(l/2) + 1):
        if l % i == 0:
            factor = l//i
            print(factor, '*', i, '=', factor * i)
            if is_prime(factor):
                return factor

print(largest_prime_factor(num))

