item1 = float(input("Enter price of the first item:"))
item2 = float(input("Enter price of the second item:"))
base = item1 + item2
base = "{:.2f}".format(base)

a = min(item1, item2)
b = max(item1, item2)
a1 = a*.5

base2 = a1 + b

tax = float(input("Enter tax rate:")) / 100

member = input('Do you have a club card? (Y/N)')

if member == "Y" or "y" or "yes":
    discount = round(base2 - (base2*.1))
    print("Base price =", base)
    print("Price after discounts =", discount)
    print("Total price =", round(discount + discount * tax, 2))
else:
    print("Base price =", base)
    print("Total price = ", round(base2 + base2 * tax, 2))
