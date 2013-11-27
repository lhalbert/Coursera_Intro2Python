# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secretNum = 0
count = 7

print "Welcome to Guess the number!"
print "----------------------------"

# helper function to start and restart the game
def new_game(range):
    global secretNum, count
    # Create secret number
    secretNum = random.randint(0,range)
    
    # Clear guess text for new game
    txtGuess.set_text("")
    
    # Reset the number of guesses
    if num_range == 100:
        count = 7
    else:
        count = 10
    
    # Print statement to start new game
    print "Guess a number between 0 and", str(range) + "!"
    print "You will only have", count, "guesses."
    print

def decrement():
    global count
    count = count - 1
    if count > 1:
        return str(count) + " guesses left."
    else:
        return str(count) + " guess left."

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, count
    num_range = 100
    count = 7
    print
    new_game(num_range)

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, count
    num_range = 1000
    count = 10
    print
    new_game(num_range)

    
def input_guess(guess):
    #print guess
    global num_range, txtGuess
    # Check to see if you have any guesses available
    if count >= 1:
        # Compare your guess to secret number
        if int(guess) == secretNum:
            print "You win!", guess, "is the right number!"
            print "-----------------------------------------"
            print
            new_game(num_range)
        elif int(guess) < secretNum:
            print guess, "is too low. Guess higher,", decrement()
            print
        else:
            print guess, "is too high. Guess lower,", decrement()
            print
    else:
        print "Game over, you guessed", str(guess) +"!", "The number was", secretNum
        print "-----------------------------------------"
        print
        new_game(num_range)
        
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
btn100 = frame.add_button("Range is [0, 100)", range100, 200)
btn1000 = frame.add_button("Range is [0, 1000)", range1000, 200)
txtGuess = frame.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
frame.start
new_game(num_range)
