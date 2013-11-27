# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
counter = 0
msgTime = "0:00.0"
attempts = 0
score = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global msgTime
    A = t // 600
    B = ((t // 10) % 60) / 10 
    C = ((t // 10) % 60) % 10 
    D = str(t)[len(str(t))-1:]
    msgTime = str(A)+":"+str(B)+str(C)+"."+str(D)
    #print msgTime[5:0]
    return msgTime
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    #print timer.is_running()

def stop():
    global attempts, score, msgTime
    timer.stop()
    
    attempts += 1
    #add a point if stopped on whole number
    if msgTime[5:] == "0":
        score += 1    
    else:
        return None
        
def reset():
    #reset all global variables to start new game
    global attempts, score, msgTime, counter
    attempts = 0
    score = 0
    msgTime = "0:00.0"
    counter = 0
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1
    format(counter)
  
    
# define draw handler
def draw(canvas):
    global time
    canvas.draw_text(msgTime,[40, 100], 50, "Green")
    canvas.draw_text("Attempts:"+str(attempts), [2,20], 20, "Red")
    canvas.draw_text("Score:"+str(score), [130,20], 20, "Red")
    
# create frame
frame = simplegui.create_frame("Stop Watch'", 200, 150)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
btnStart = frame.add_button("Start", start, 50)
btnStop = frame.add_button("Stop", stop, 50)
btnReset = frame.add_button("Reset", reset, 50)

frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
