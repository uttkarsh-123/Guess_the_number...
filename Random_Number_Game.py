import random
print("\t\t\t\"THIS IS A NUMBER GUESSING GAME!!!\"")
upper_lim = int(input("You want to guess from 0 till which number?\n"))
random_num = int(random.random()*upper_lim)
lives = int(input("How many lives do you want? \n =>"))
guess = int(input("Please guess the random number:- \n"))
lives = lives-1
while(True):
    if guess == random_num:
        print("Congratulations, you have guessed the correct number with", lives, "lives left.")
        break
    if lives<=0:
        print("Sorry, your lives are finished.")
        break
    if guess>random_num:
        print("Please decrease the value of your guess.\t\t\t\t Lives left =", lives)
        guess = int(input())
        lives = lives-1
    elif guess<random_num:
        print("Please increase the value of your guess.\t\t\t\t Lives left =", lives)
        guess = int(input())
        lives = lives-1
