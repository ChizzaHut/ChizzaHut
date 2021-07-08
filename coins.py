print("Please enter the amount of money to convert: ")

dollar = int(input("# of Dollars: ")) * 100
cents = int(input("# of cents: "))

total = (dollar + cents) / 100

quarters = total // .25
r1 = (total - (quarters * .25))

dimes = r1 // 0.1
r2 = (r1 - (dimes * 0.1))

nickels = (r2 // .05)
r3 = (r2 - (nickels * .05))

pennies = r3 * 100
p = "{:.1f}".format(pennies)

print("the coins are", quarters, "Quarters,", dimes, "Dimes,",
      nickels, "Nickels and", p, " pennies")
