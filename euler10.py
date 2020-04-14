'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

lim = 2_000_000

N = {i for i in range(2, lim)} - { j for i in range(2, lim//2 + 1) for j in range(2*i, lim + 1, i)}

print(sum(N))
