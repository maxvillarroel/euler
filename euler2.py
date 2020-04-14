
i = 0
j = 1
h=0
sum = 0
lim = 4000000
while h < lim:
    h = i + j
    if h % 2 == 0 and h < lim:
        sum += h
    i = j
    j = h

print(sum)
