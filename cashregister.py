item1 = float(input("Enter price of the first item:"))
item2 = float(input("Enter price of the second item:"))
base = item1 + item2
base = "{:,.2f}".format(base)

a = min(item1, item2)
b = max(item1, item2)
a1 = a*.5

base2 = a1 + b

member = str(input('Do you have a club card?'))

tax = float(input("Enter tax rate:")) / 100

total2 = base2 + (base2 * tax)
total2 = "{:,.2f}".format(total2)

if member == 'y' or 'Y' or 'yes' or 'Yes':
    y = (base2 - (base2 * 0.10))
    total = float(y + y * tax)
    total = "{:2.2f}".format(total)

    print("Base price =", base)
    y = "{:2.2f}".format(y)
    print("Price after discounts =", y)
    print("Total price =", total)

elif member != 'y' or 'Y' or 'yes' or 'Yes':
    print("Base price =", base)
    print("Total price = ", total2)
