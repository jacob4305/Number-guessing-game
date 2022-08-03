import random

player_score = []
print("Welcome to the number guessing game!!")
 

def start_game():


    random_number = random.randint(1, 10)
    guesses = 0

    while True:
        if player_score != []:
            top_score = player_score[0]
            print("The current top score is {}".format(top_score))

        if player_score == []:
            print("There is no current top score")
        try:
            user_guess = int(input("Guess what number im thinking of?: "))
        except ValueError:
            print("Please enter a number")
            continue
        if user_guess > 10:
            print("number cant be over 10")
            continue
        if user_guess < 1:
            print("number cant be under 1")
            continue
        if user_guess > random_number:
            guesses += 1
            print("Its lower")
        if user_guess < random_number:
            guesses += 1
            print("Its higher")
        if user_guess == random_number:
            guesses += 1
            print("You got it, it took you {} guesses".format(guesses))
            player_score.append(guesses)
            player_score.sort()                                  
            break

                                               

def play_again():


    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y".lower():
            start_game()
        elif play_again == "n".lower():
            print("Thanks for playing!!!")
            break
        else:
            print("Please enter either y or n")
            continue

start_game()
play_again()