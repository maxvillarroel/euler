multOf3 = set()
multOf5 = set()

for i in range(0, 1000, 3):
    multOf3.add(i)

for i in range(0, 1000, 5):
    multOf5.add(i)

multOf3.discard(0)
multOf5.discard(0)

multOf3or5 = multOf3.union(multOf5)


ans=0

for i in multOf3or5:
    ans += i

print(ans)
