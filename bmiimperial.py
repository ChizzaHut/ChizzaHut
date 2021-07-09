weight = float(input("Enter your weight in pounds: "))
w = weight * 0.453592
height = float(input("Enter your height in inches: "))
h = height * .0254

BMI = w / (h**2)

print("Your BMI is", BMI)