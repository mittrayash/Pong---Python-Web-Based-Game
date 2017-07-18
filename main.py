# Implementation of classic arcade game Pong
# Note: Run this code live at http://www.codeskulptor.org
# The support for this code is via the codeskulptor interactivity framework which the code relies on.

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400     
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = random.choice([True, False])
RIGHT = not LEFT
paddle1_vel = paddle2_vel = 0
if LEFT == True:
    direction = LEFT
else:
    direction = RIGHT
score1 = score2 = 0

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [1, 2]

paddle1_posd = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle1_posu = [HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle2_posd = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle2_posu = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]


# if direction is RIGHT, the ball's velocity is upper right, else upper lef
def vel(dir):
	if dir == RIGHT:
        ball_vel[0] = random.randrange(2, 6)
    elif dir == LEFT:
        ball_vel[0] = -random.randrange(2, 6)
ball_vel[1] = -random.randrange(3, 7)


def spawn_ball(directio):
    global ball_pos, ball_vel, direction# these are vectors stored as lists
    directio = random.choice([LEFT, RIGHT])
    vel(directio)



def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos # these are numbers  
    global score1, score2 # these are ints
    score1 = score2 = 0
	directio = random.choice([LEFT, RIGHT])
	ball_pos = [WIDTH/2, HEIGHT/2]
    spawn_ball(directio)
	
def restart1():
    new_game()	

	
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
	
	# draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
	
# define event handlers

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# start frame
new_game()
frame.start()
