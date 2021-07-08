print("Please enter the number of coins: ")

quarter = int(input("# of Quarters: ")) * 25
dimes = int(input("# of Dimes: ")) * 10
nickels = int(input("# of Nickels: ")) * 5
pennies = int(input("# of Pennies: "))

total = quarter + dimes + nickels + pennies
dollars = total // 100
cents = total % 100
print("The total is ",dollars,"dollars and ",cents,"cents")