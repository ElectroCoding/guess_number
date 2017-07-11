#!/c/python27/python
""" This Program is a Guessing Game
It prompts the user to guess a number 
between 1 and 100 
"""

# Guessing Game - guess_number.py

def main():
    print "Guess a number between 1 and 100"
    randomNumber = 35
    found = False   #flag variable to see
                    #if they guessed it

    while not found:
        userGuess = input("Your Guess: ")
        if userGuess == randomNumber:
            print "You got it!"
            found = True
        elif userGuess > randomNumber:
            print "Guess Lower"
        else:
            print "Guess Higher"

main()