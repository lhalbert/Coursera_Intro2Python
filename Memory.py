# implementation of card game - Memory

import simplegui
import random
import math

#Global Variables
HEIGHT = 100
WIDTH = 800
CARDWIDTH = 50
CARDHEITH = 100
numlist = ""
card_deck = []
clicklist = []
dump = ""
state = 0
cardpos = [25, 50]
txtpos = [5, 75]
count = 0
turns = 0
hidden = 0 

# helper function to initialize globals
def new_game():
    global cardpos, txtpos, state, count, numlist, cardlist, card_deck, turns
    numlist = ""
    card_deck = []
    clicklist = []
    state = 0
    cardpos = [25, 50]
    txtpos = [5, 75]
    count = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    genNums()
    genCards()

# create number order
def genNums():
    global numlist
    numlist = range(0,8)+range(0,8)
    random.shuffle(numlist)
    #print numlist
    return numlist

# create deck of cards
def genCards():
    global cardpos, txtpos
    for num in numlist:  
        #List value (number, (text_position), (card_position), Hide_value, Match_value)
        card_deck.append([num,[txtpos[0],txtpos[1]],[cardpos[0],cardpos[1]],True,False])
        txtpos[0] += 50
        cardpos[0] += 50  
    
# define event handlers
def mouseclick(pos):
    global clicklist, turns, state, dump
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
        #update # of turns label
        turns += 1
        label.set_text("Turns = " + str(turns))
    else:
        state = 1
    #unhide cards that are clicked
    count = 0
    for card in card_deck:
        if (pos[0] < card_deck[count][2][0]+25) and (pos[0] > card_deck[count][2][0] -25):
            #Set hide value to false
            card_deck[count][3] = False
            clicklist.append([count,card])
        count += 1
    
    if len(clicklist) == 2:
        #Check to see if cards are the same
        if clicklist[0][1][0] == clicklist[1][1][0]:#Set Match value to true
            card_deck[clicklist[0][0]][4] = True
            card_deck[clicklist[1][0]][4] = True
            #increment dump string to compare to list length later in draw
            dump += str(card_deck[clicklist[0][0]][0])
            dump += str(card_deck[clicklist[1][0]][0])
    elif len(clicklist) == 3:
        if clicklist[0][1][0] == clicklist[1][1][0]:
            #Set Match value to true
            #card_deck[clicklist[0][0]][4] = True
            #card_deck[clicklist[1][0]][4] = True
            clicklist.pop(0)
            clicklist.pop(0)

        else:
            #Set hide value to true
            card_deck[clicklist[0][0]][3] = True
            card_deck[clicklist[1][0]][3] = True
            #remove first two cards from list
            clicklist.pop(0)
            clicklist.pop(0)
             
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global count
    count = 0
    
    for num in card_deck:
        canvas.draw_text(str(card_deck[count][0]), [card_deck[count][1][0], card_deck[count][1][1]]
                         , 75, "Green")
        
        # if match value is true, then color red and cross out
        if card_deck[count][4]:
            if len(dump) == len(card_deck):
                canvas.draw_polygon([[0,0],[WIDTH,0],[WIDTH,HEIGHT],[0,HEIGHT]], 1, "Black", "Black")
                canvas.draw_text("You Win!", [250, 75], 75, "Red")
            else:
                canvas.draw_text(str(card_deck[count][0]), [card_deck[count][1][0], card_deck[count][1][1]]
                         , 75, "Red")
                canvas.draw_line([card_deck[count][2][0]+25, card_deck[count][2][1]-50],
                             [card_deck[count][2][0]-25, card_deck[count][2][1]+50], 2, "red")
        # if hide value is true, then fill in card
        else:
            if card_deck[count][3]:
                canvas.draw_polygon([[card_deck[count][2][0]-25, card_deck[count][2][1]-50], 
                                 [card_deck[count][2][0]+25, card_deck[count][2][1]-50], 
                                 [card_deck[count][2][0]+25, card_deck[count][2][1]+50], 
                                 [card_deck[count][2][0]-25, card_deck[count][2][1]+50]], 2, 'black', "green")                            
            else:
                canvas.draw_polygon([[card_deck[count][2][0]-25, card_deck[count][2][1]-50], 
                                 [card_deck[count][2][0]+25, card_deck[count][2][1]-50], 
                                 [card_deck[count][2][0]+25, card_deck[count][2][1]+50], 
                                 [card_deck[count][2][0]-25, card_deck[count][2][1]+50]], 1, 'green') 
        count += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
