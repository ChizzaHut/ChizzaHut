item1 = float(input("Enter price of the first item:"))
item2 = float(input("Enter price of the second item:"))
base = item1 + item2
base = "{:,.2f}".format(base)

a = min(item1, item2)
b = max(item1, item2)
a1 = a * .5

base2 = a1 + b

# Make variables for Y and N
member = input('Does customer have a club card? (Y/N):')

is_a_member = 0
# Yes category
if member == 'y' or member == 'Y' or member == 'yes' or member == 'Yes':
    is_a_member = 1

# No category
elif member == 'n' or member == 'N' or member == 'no' or member == 'No':
    is_a_member = 2

tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax:")) / 100

total2 = base2 + (base2 * tax)
total2 = "{:,.2f}".format(total2)

if is_a_member == 1:
    discount = (base2 - (base2 * 0.10))
    total = float(discount + discount * tax)
    total = "{:2.2f}".format(total)
    discount = "{:2.2f}".format(discount)
    base2 = "{:,.2f}".format(base2)

    print("Base price =", base, "Price after discounts =", discount, "Total price =", total)

elif is_a_member == 2:
    base2 = "{:,.2f}".format(base2)
    print("Base price =", base, "Price after discounts =", base2, "Total price =", total2)

else:
    print("Invalid")

