a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for num in a:
    if num in b:
        if num not in c:
            c.append(num)
c.sort
print(a)
print(b)
print("The common numbers between both lists are:")
print(c, "\n\nDone")

import random

d = random.sample(range(1, 50), 12)
e = random.sample(range(1, 50), 10)
f = []

for num in d:
    if num in e:
        if num not in f:
            f.append(num)
f.sort
print(d)
print(e)
print("The common numbers between both lists are:")
print(f)
