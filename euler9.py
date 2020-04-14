'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#ls = [ (a,b,c) for a,b,c in range(1000) if a<b<c and a+b+c == 1000 and a*a+b*b==c*c]
lim = 1000

ls = [ print(a*b*(lim - a - b)) for a in range(1, lim - 1) for b in range(a + 1, lim - a - 1) if a**2 + b**2 == (lim - a - b)**2 ]
