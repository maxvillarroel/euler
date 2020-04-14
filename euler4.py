count = []
for i in range(100, 1000):
    for j in range(i, 1000):
        count.append(i*j)

count.sort(reverse = True)

def is_palindrome(n):
    i = int(str(n)[::-1])
    if i == n:
        return True
    return False

for i in count:
    if is_palindrome(i):
        print(i)
        break

