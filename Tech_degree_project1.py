import random

random_number = 0

def start_game():
    
    print("Welcome to the number guessing game!".title())
    
    random_number = random.randint(1, 11)
    attempts = 0
    
    while True:
        try:
            user_input = int(input("{}Try to guess what number im thinking of!{}Hint(Its between 1 and 10) ==>  ".format("\n", "\n")))
        except ValueError as ve:
            print("{}Please enter a NUMBER between 1 and 10".format("\t").upper())
            continue
        if user_input > 10:
            print("{}{}Number has to be 10 or lower".format("\n", "\t").upper())
            continue
        if user_input > random_number:
            print("{}{}Its lower".format("\n", "\t").upper())
        if user_input < random_number:
            print("{}{}Its higher".format("\n", "\t").upper())
        elif user_input == random_number:
            attempts += 1
            print("{}{}YOU GOT IT!!!, it took you {} guesses!".format("\n", "\t", attempts))
            break
            
        attempts += 1

    print("{}------Thanks for playing!!!------".format("\n").upper())
                           
    
start_game()
