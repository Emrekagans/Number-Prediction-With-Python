import random, time

number_of_predictions = 5

# Functions

def countdown():
    for i in range(3,0,-1):
        time.sleep(1)
        print(i)
    time.sleep(1)

def exit():
    print("Game ending")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)


def start_again():
    print("The Game Begins Again")
    time.sleep(0.5)
    start_game()

def start_game():
    number_of_predictions = 5

    print("The game is about to begin...")
    countdown()
    print("Don't forget you get 5 guesses!!")

    right_number = random.randint(0,100)

    while(number_of_predictions>0):
        your_prediction = int(input("I kept a number in my mind between 0-100. Lets guess!!: "))
        if(your_prediction>right_number):
            print("the number I have in mind is lower than your prediction: ")
            number_of_predictions -= 1

        elif(your_prediction<right_number):
            print("the number I have in mind is higher than your prediction: ")
            number_of_predictions -= 1

        else:
            print("Congratulations... You guessed the number I had in my mind")
            print("The number I kept in my mind was: " + str(right_number))
            break

    if(number_of_predictions==0):
        print("You're out of guesses")
        print("The number I kept in my mind was: " + str(right_number))

    play_again = input("Do you want to play again? If you want to play again, press the (Y) button, if not, press the (N) button: ")

    if(play_again == "Y" or play_again == "y"):
        start_again()

    elif(play_again == "N" or play_again == "n"):
        exit()

    else:
        print("Good Byee...")
        exit()

start_game()