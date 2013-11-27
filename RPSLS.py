# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Not a valid number!"
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Not a valid name!"

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_num = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_num = random.randrange(0, 4)
    
    # compute difference of player_number and comp_number modulo five
    score = (player_num - comp_num) % 5
    #print score
    
    # use if/elif/else to determine winner
    if score == 0: #Did both players choose the same
        winner = "Player and computer tie!"
    elif score >= 3:
        winner = "Computer wins!"
    else:
        winner = "Player wins!"

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_num)
    
    """
    Not sure why I would use the number_to_name function in the print
    statements when I already have name parameter and comp_name from
    number_to_name above - but rubric said so!
    """
    # print results
    print "Player chooses", number_to_name(player_num)
    print "Computer chooses", number_to_name(comp_num)
    print winner
    print ""
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
