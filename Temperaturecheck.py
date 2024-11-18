##Temperature Check
temperature = float(input("Enter the current outdoor temperature: "))

if temperature>= 30:
    print("It's hot!")
elif 15 <= temperature < 30:
    print("It's warm.")
else:
    print("It's cold.")
