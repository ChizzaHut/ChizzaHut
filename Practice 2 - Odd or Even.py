num = int(input("Print a number: "))
check = int(input("Print a number to divide by: "))
mod = num%2
if num%4 == 0:
    print("Your number is divisible by 4")
elif mod == 0:
    print("Your number is even")
else:
    print("Your number is odd")

if num%check == 0:
    print("Your number", num, "divides evenly with", check)
else:
    print("Your number", num, "does not divide evenly with", check)
