user_choice = "y"
while user_choice == "y":
    num1 = input("Please enter a number to prime factorise it :-\n")
    num2 = num1
    if num1.isnumeric() == False:
        print("Please enter a valid input...")
        continue
    num1 = int(num1)
    num2 = int(num2)
    prime_factors = []
    divisor = 2
    while divisor <= num1:
        if num1 % divisor == 0:
            num1 = num1 / divisor
            prime_factors.append(divisor)
        else:
            divisor = divisor + 1
    for i in prime_factors:
        print(i, "\t", int(num2))
        num2 = num2 / i
    print("\t", 1)
    while True:
        user_choice = input("Do you want to prime factorise some other number as well? Type \'y\' for yes and \'n\' for no:- \n")
        if user_choice != 'y' and user_choice != 'n':
            print("Please enter a valid input.....")
        else:
            break