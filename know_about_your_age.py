print("This program tells you a lot about your age...")
age_or_year_of_birth = int(input("Please enter your age or year of birth :-\n"))
if age_or_year_of_birth>1900 and age_or_year_of_birth<2021:
    print("Ok, so your age will be 100 in the year", age_or_year_of_birth+100, ".")
    user_wish = str(input("Do you want to know that what will be your age in a given year? Enter \'y\' for yes and \'n\' for no. \n"))
    while (True):
        if user_wish == "y":
            print("Ok, so please enter the year.")
            user_year = int(input())
            print("Your age in the year", user_year, "="  , user_year - age_or_year_of_birth )
            print("Do you want to know your age in some other year as well? Please enter \'y\' for yes and \'n\' for no.")
            user_wish_2 = input()
            if user_wish_2 == "y":
                continue
            else:
                print("Thanks for using our program, have a nice day!!")
                break
if age_or_year_of_birth > 2021:
    print("You are not born yet!!!!")
elif age_or_year_of_birth > 120 and age_or_year_of_birth < 1900:
    print("You seem to be the oldest person alive!!!!")
    print("Do you want to specify a particular year and calculate your age in that year? Please type \'y\' for yes and \'n\' for no.")
    yes_or_no = input()
    while (True):
        if yes_or_no == "y":
            print("Ok, please specify the year....")
            year = int(input())
            x = year-2021
            print("Your age in the year", year, "=", age_or_year_of_birth + x)
            print("Do you want to specify some other year as well? Press \'y\' for yes and \'n\' for no!!")
            y_N = input()
            if y_N == "y":
                continue
            elif y_N == "n":
                print("Thanks for using our program......")
                break
            else:
                print("Please enter a valid input...")
                continue
        else:
            print("Ok, thanks for using our program..")
            exit()
else:
    print("Alright, so your age will be 100 in the year", (100-age_or_year_of_birth)+2021)
    user_wish = str(input("Do you want to know that what will be your age in a given year? Enter \'y\' for yes and \'n\' for no. \n"))
    while(True):
        if user_wish == "y":
            print("Ok, so please enter the year:-")
            user_input_year = int(input())
            year_of_birth = 2021 - age_or_year_of_birth
            final_age = user_input_year - year_of_birth
            print("Your age in the year", user_input_year, "=", final_age)
            print("Do you want to calculate some other year as well? press \'y\' for yes and \'n\' for no.")
            yes_no = str(input())
            if yes_no == "y":
                continue
            else:
                print("Thanks for using our program..")
                break
        else:
            print("Ok, thanks for using our program, have a nice day ahead!")