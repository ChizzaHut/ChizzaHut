item1 = float(input("Enter price of the first item:"))
item2 = float(input("Enter price of the second item:"))
base = item1 + item2
base = "{:,.2f}".format(base)

a = min(item1, item2)
b = max(item1, item2)
a1 = a*.5

base2 = a1 + b
# Make variables for Y and N
member = input('Does customer have a club card? (Y/N):')
# Yes category
if member == 'y':
    member = 1
elif member == 'Y':
    member = 2
elif member == 'yes':
    member = 3
elif member == 'Yes':
    member = 4
# No category
elif member == 'n':
    member = 6
elif member == 'N':
    member = 7
elif member == 'no':
    member = 8
elif member == 'No':
    member = 8

tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax:")) / 100

total2 = base2 + (base2 * tax)
total2 = "{:,.2f}".format(total2)

if member < 5:
    discount = (base2 - (base2 * 0.10))
    total = float(discount + discount * tax)
    total = "{:2.2f}".format(total)
    discount = "{:2.2f}".format(discount)

    print("Base price =", base, "Price after discounts =", discount, "Total price =", total)

elif member > 5:
    print("Base price =", base, "Total price =", total2)
