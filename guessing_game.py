import random

# game setup
print("welcome to the guessing game")
number_of_guesses = 3 # user has 3 guesses before losing the game
user_won = False

# computer guesses random number between 1 and 10
correct_answer = random.randint(1, 10)


while number_of_guesses > 0:
    # user guesses the number
    user_guess = input("Please enter your guess: ")
    user_guess = int(user_guess)

    # computer tells user whether guess was too high or too low
    if user_guess == correct_answer:
        print("good guess!")
        print("you are correct")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("sorry you guessed too high")
    elif user_guess < correct_answer:
        print("sorry you guessed too low")
    else:
        print("incorrect")

    number_of_guesses -= 1

if user_won == True:
    print("you win!")
else:
    print("you lose!")
