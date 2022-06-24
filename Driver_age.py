print("Enter your age:-")
age = int(input())
if 121 > age > 18:
    print("You can drive.")
elif 3 < age < 18:
    print("You are too young to drive.")
elif age == 18:
    print("You have to give a physical test.")
else:
    print("Enter a logical age.")
input("Press enter to exit the program:-\n")