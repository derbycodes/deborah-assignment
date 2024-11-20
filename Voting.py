age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18 and country.lower() == "ghana":
    print("You can vote")
else:
    print("You cannot vote")
