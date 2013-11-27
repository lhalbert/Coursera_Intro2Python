# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [random.randrange(-4, 4), random.randrange(-4, 4)]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0
paddle1_pos = [HALF_PAD_WIDTH, (HEIGHT/2)]
paddle1_vel = [0]
paddle2_pos = [WIDTH- HALF_PAD_WIDTH, (HEIGHT/2)]
paddle2_vel = [0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == False:
        ball_vel = [random.randrange(2, 4)* -1, random.randrange(1, 3) * -1]
    else:
        ball_vel = [random.randrange(2,4), random.randrange(1,3) * -1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, (HEIGHT/2)]
    paddle1_vel = [0]
    paddle2_pos = [WIDTH- HALF_PAD_WIDTH, (HEIGHT/2)]
    paddle2_vel = [0]
    score1 = 0
    score2 = 0
    
    #Randomly start the ball to either left or right
    spawn_ball(random.choice([RIGHT, LEFT]))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
      
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Red") #Center Line
    c.draw_line([WIDTH / 2 - 100, 0],[WIDTH / 2 - 100, HEIGHT], 1, "Blue") #Left Blue Line
    c.draw_line([WIDTH / 2 + 100, 0],[WIDTH / 2 + 100, HEIGHT], 1, "Blue") #Right Blue Line
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Blue") #Left Gutter
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Blue") #Right Gutter
    c.draw_circle([WIDTH / 2, HEIGHT / 2], 75, 1, "Blue") #Center
    c.draw_circle([WIDTH / 2, HEIGHT / 2], 5, 1, "Red", "Red") #Upper Left Center
    c.draw_circle([100, 75], 40, 1, "Blue") #Upper Left
    c.draw_circle([100, 75], 5, 1, "Red", "Red") #Upper Left Center
    c.draw_circle([100, HEIGHT - 75], 40, 1, "Blue") #Lower Left
    c.draw_circle([100, HEIGHT - 75], 5, 1, "Red", "Red") #Lower Left Center
    c.draw_circle([WIDTH - 100, HEIGHT - 75], 40, 1, "Blue") #Lower Right
    c.draw_circle([WIDTH - 100, HEIGHT - 75], 5, 1, "Red", "Red") #Lower Right Center           
    c.draw_circle([WIDTH - 100, 75], 40, 1, "Blue") #Upper Right
    c.draw_circle([WIDTH - 100, 75], 5, 1, "Red", "Red") #Upper Right Center           
    
    
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
  
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        
        #If the ball is not within the vertical limits of the paddle, score or speed up
        if  abs(paddle1_pos[1] - ball_pos[1]) > 40:
            score2 += 1
            spawn_ball(True)
        else:
            ball_vel[0] += ball_vel[0] * .1
            ball_vel[1] += ball_vel[1] * .1
                 
    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= (WIDTH-(1+PAD_WIDTH)) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0] 
        
        #If the ball is not within the vertical limits of the paddle, score or speed up
        if  abs(paddle2_pos[1] - ball_pos[1]) > 40:
            score1 += 1
            spawn_ball(False)
        else:
            ball_vel[0] += ball_vel[0] * .1
            ball_vel[1] += ball_vel[1] * .1
            
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Black")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[0]
    paddle2_pos[1] += paddle2_vel[0]
   
    #ensure that left paddle stays on the table
    if paddle1_pos[1] <= HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
        paddle1_vel[0] = 0
    elif paddle1_pos[1] >= HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        paddle1_vel[0] = 0
        
    #ensure that right paddle stays on the table
    if paddle2_pos[1] <= HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
        paddle2_vel[0] = 0
    elif paddle2_pos[1] >= HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        paddle2_vel[0] = 0
           
    # draw paddles    
    Pad1 = c.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "Black")    
    Pad2 = c.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "Black")
    
    # draw scores
    left_score = c.draw_text(str(score1), [WIDTH/2 - 60, 55], 40, "Black")
    right_score = c.draw_text(str(score2), [WIDTH/2 + 40, 55] , 40, "Black")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    move = 6
    #Move left paddle
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= move
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += move
    #Move right paddle    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= move 
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += move
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    move = 0
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] = move
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] = move   
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] = move 
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] = move
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("white")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)

# start frame
#new_game()
frame.start()
