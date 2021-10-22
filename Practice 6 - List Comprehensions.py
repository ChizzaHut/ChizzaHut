import random

a = random.sample(range(1, 50), 10)
a.sort()
b = []
c = []
for x in a:
    if x % 2 == 0:
        b.append(x)
    else:
        c.append(x)
print(a)
print(b)

