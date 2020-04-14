"""

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 ... + 10^2= 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
def sum_of_sqr(n):
    sum = 0
    for i in range(n + 1):
        sum += i*i
    print(sum)
    return sum

def sqr_of_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    print(sum*sum)
    return sum*sum

print(sqr_of_sum(100)-sum_of_sqr(100))
