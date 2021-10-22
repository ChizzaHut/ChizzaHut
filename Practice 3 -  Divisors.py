divisor = int(input("Please enter a number: "))
lstRang = list(range(1, divisor+1))
lst = []

for elem in lstRang:
    if divisor % elem == 0:
        lst.append(elem)
print(lst)
