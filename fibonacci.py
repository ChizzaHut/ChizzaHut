n = int(input("Please enter a positive integer greater than 1:"))
# Create first variable for the sequence
count1 = 0
# Create second variable for the sequence
count2 = 1
print(count2)

for i in range(1, n):
    fibnum = count1 + count2
    print(fibnum)
    count1 = count2
    count2 = fibnum
