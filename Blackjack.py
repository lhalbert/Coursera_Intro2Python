# Mini-project #6 - Blackjack

import simplegui
import random

WIDTH = 600
HEIGHT = 600
# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = 0
score_value = "Score"
bet = 1
dealer_pos = [20, 230]
player_pos = [20, 400]
d_value = "Dealer"
p_value = "Player"


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        s = ""
        for c in self.hand:
            s = s + " " + str(c)
        return "Hand contains " + s

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        Aces = False
        for c in self.hand:
            hand_value += VALUES[str(c)[-1:]]
            if str(c)[-1:] == "A":
                Aces = True
        if Aces:
            if(hand_value + 10) <= 21:
                hand_value += 10
        return hand_value

    def reset(self):
        self.hand = []
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas,pos)
            pos[0]+=CARD_SIZE[0]
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        dealt_card = self.deck[0]
        self.deck.remove(self.deck[0])
        return dealt_card

    def reset(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
        
    def __str__(self):
        # return a string representing the deck
        d = ""
        for c in self.deck:
            d = d + " " + str(c)
        return "Deck contains: " + d

#define event handlers for buttons
def new_deal():
    global d_value, p_value, outcome, bet, in_play
    # build new deck and empty hands
    the_deck.reset()
    player.reset()
    dealer.reset()
    
    # Reset the player labels without scores
    d_value = "Dealer"
    p_value = "Player"
    in_play = False
    outcome = "Hit or Stand?"
    
    # check to bet input value
    if bet_value.get_text() == "":
        bet = 1
    else:
        bet = int(bet_value.get_text())

    # deal new hands
    deal(the_deck, player, dealer)
    
def deal(the_deck, player, dealer):
    global outcome, in_play, d_value, p_value

    # Deal the cards
    the_deck.shuffle()
    print the_deck
    player.add_card(the_deck.deal_card())
    player.add_card(the_deck.deal_card())
    dealer.add_card(the_deck.deal_card())
    dealer.add_card(the_deck.deal_card())
    in_play = True

def hit():
    global outcome, in_play, score, d_value, p_value  
 
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(the_deck.deal_card())
         # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "You are bust!"
            score -= bet
            in_play = False
            d_value = "Dealer has "+ str(dealer.get_value())
            p_value = "Player has "+ str(player.get_value())
    else:
        return None
     
def stand(): 
    global outcome, score, in_play, d_value, p_value
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(the_deck.deal_card())
        else:
            if dealer.get_value() <= 21:
                if dealer.get_value() >= player.get_value():
                    outcome = "Dealer Wins!"
                    score -= bet
                    in_play = False
                    d_value = "Dealer has "+ str(dealer.get_value())
                    p_value = "Player has "+ str(player.get_value())
                else:
                    outcome = "You win!"
                    in_play = False
                    score += bet
                    d_value = "Dealer has "+ str(dealer.get_value())
                    p_value = "Player has "+ str(player.get_value())
            else:
                outcome = "You win!"
                in_play = False
                score += bet
                d_value = "Dealer has "+ str(dealer.get_value())
                p_value = "Player has "+ str(player.get_value())

# draw handler    
def draw(canvas):
    global outcome
    # set up game table
    canvas.draw_text("BlackJack", [10, 50], 40, "Black")
    canvas.draw_text("Score: "+str(score), [400, 50], 40, "Black")
    canvas.draw_text(outcome, [WIDTH/3, 575], 50, "Red")
    canvas.draw_text("Current Bet: "+ str(bet), [10, 120], 30, "White")
    
    
    # draw dealer
    canvas.draw_text(d_value, [20, 220], 40, "Gold")
    dealer_pos = [20, 230]
    dealer.draw(canvas, dealer_pos)
    
    # draw player
    canvas.draw_text(p_value, [20, 390], 40, "Gold")
    player_pos = [20, 400]
    player.draw(canvas, player_pos)

    # cover dealers first card until hand is over
    # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [20+CARD_BACK_CENTER[0] , 230+CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
def bet_handler(text_input):
    global bet
    if text_input == "":
        bet = 1
    elif int(text_input):
        bet = int(text_input)
    else:
        print "Bet is not a valid number." 
        print "Seting game to points."

#Global variables
the_deck = Deck()
player = Hand()
dealer = Hand()

# initialization frame
frame = simplegui.create_frame("Blackjack", WIDTH, HEIGHT)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", new_deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
bet_value = frame.add_input("How much do you want to bet?", bet_handler, 50)
frame.set_draw_handler(draw)


# get things rolling

deal(the_deck, player, dealer)
frame.start()


# remember to review the gradic rubric
