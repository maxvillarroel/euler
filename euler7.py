'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
'''
pi(n)= n/ln(n = 10_001)
n=116684
'''
from matplotlib import pyplot as plt
from math import log
#Try with the sieve of Erastothenes
#n = 116_684
n = 116_684
N = { i for i in range(2, n + 1)}

for i in range(2, n//2 + 1):
    sieve = {j for j in range(i, n + 1, i)}
    sieve.remove(i)
    N -= sieve

print('The first', len(N), 'primes were generated')
y = [i for i in range(1, len(N) + 1)]
x = sorted(N)
y2 = [i/log(i) for i in x]
plt.plot(x, y)
plt.plot(x, y2)
plt.show()
