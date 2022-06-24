import random
print("This is stone, paper, scissors game!")
user_input_str = input("Type \'r\' to read the rules and any other key to continue!\t")
if user_input_str == 'r' or user_input_str == 'R':
    print("\n\n\n\n\nThe user will specify a point limit and whosesoever reaches that point limit first, wins the game! Chose anything : Stone, Paper or Scissors. \n Stone breaks scissors, but gets wrapped by paper. \n Paper wraps stone, but gets cut by scissors. \n Scissors cut paper, but gets broken by stone.")
while True:
    points = int(input("\n\n\n\n\n\nNow as you know the rules, please enter the point limit :-\n"))
    comp_points = 0
    user_points = 0
    while True:
        if comp_points == points or user_points == points:
            break
        r_num = int(random.random()*3)+1
        user_input = int(input("*Type :-\n\'1\' to choose stone\n\'2\' to choose paper\n\'3\' to choose scissors\n=>"))
        if r_num == 1:
            if user_input == 1:
                print("The computer also chose stone and it's a tie!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
            elif user_input == 2:
                user_points += 1
                print("The computer chose stone and congratulations, you won!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
            else:
                comp_points += 1
                print("The computer chose stone and sorry, you lost!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
        elif r_num == 2:
            if user_input == 1:
                comp_points += 1
                print("The computer chose paper and sorry, you lost!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
            elif user_input == 2:
                print("The computer also chose paper and it's a tie!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
            else:
                user_points += 1
                print("The computer chose paper and congratulations, You won!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
        else:
            if user_input == 1:
                user_points += 1
                print("The computer chose scissors and congratulations, you won!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
            elif user_input == 2:
                comp_points += 1
                print("The computer chose scissors and sorry, you lost!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
            else:
                print("The computer also chose scissors and it's a tie!","\t\t\tComputer Score =",comp_points,"\t\t\tUser Score =",user_points)
    if user_points == points:
        print("You finally defeated the computer! We would like to give you the heartiest congratulations on this unrealistic acheivement!")
    else:
        print("\n\n\n\nYou got defeted by the computer! We're really sorry for that and we also feel sad for you. We wish you all the very best for next time!")
    user_choice = input("Press \'y\' to play again and any other key to quit the game!")
    if user_choice == 'y':
        continue
    else:
        exit()