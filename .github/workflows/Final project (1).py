#!/usr/bin/env python
# coding: utf-8

# In[18]:


import turtle as trt
trt.reset()


# In[19]:


import turtle as trt
import time

def get_color(color):
    colors = {'red':(1,0,0),
              'white':(1,1,1),
              'blue':(0,0,1),
              'black':(0,0,0)}
    return colors[color]

# create a screen
screen = trt.getscreen()
# set background color of screen
screen.bgcolor(get_color('white'))
# set title of screen
screen.title("USA Flag by Izzy and Kate")
trt = trt.Turtle()
# set the cursor/turtle speed
trt.speed(500)
trt.penup()
# flag height to width ratio is 1:1.9
flag_height = 250
flag_length = 475

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -237
start_y = 125

# For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
stripe_height = flag_height/13
stripe_length = flag_length

# length of one arm of star
star_size = 10

def draw_rectangle(x, y, height, length, color):
    trt.pencolor(get_color('black'))
    trt.goto(x,y)
    trt.pendown()
    trt.color(color)
    trt.begin_fill()
    trt.forward(length)
    trt.right(90)
    trt.forward(height)
    trt.right(90)
    trt.forward(length)
    trt.right(90)
    trt.forward(height)
    trt.right(90)
    trt.end_fill()
    trt.penup()
    trt.hideturtle()

def draw_star(x, y, col, length):
    trt.goto(x,y)
    trt.setheading(0)
    size = 3
    trt.color(get_color('white'))
    trt.width(2)
    angle = 144
    trt.fillcolor(get_color('white'))
    trt.begin_fill()
    for side in range(5):
        trt.pendown()
        trt.fd(size)
        trt.rt(angle)
        trt.fd(size)
        trt.rt(72 - angle)
        trt.penup()
    trt.end_fill()

# this function is used to create 13 red and white stripes of flag
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 13 stripes, 7 red and 6 white
    # so we first create, 6 red and 6 white stripes alternatively    
    for stripe in range(0,6):
        for color in [get_color('red'), get_color('white')]:
            draw_rectangle(x, y, stripe_height, stripe_length, color)
            # decrease value of y by stripe_height
            y = y - stripe_height            

    # create last red stripe
    draw_rectangle(x, y, stripe_height, stripe_length, get_color('red'))
    y = y - stripe_height


# this function create navy color square
# height = 7/13 of flag_height
# width = 0.76 * flag_height
# check references section for these values
def draw_square():
    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height
    draw_rectangle(start_x, start_y, square_height, square_width, get_color('blue'))


def draw_six_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 112
    # create 5 rows of stars
    for row in range(0,5) :
        x = -222
        # create 6 stars in each row
        for star in range (0,6) :
            trt.fillcolor(get_color('white'))
            trt.begin_fill()
            draw_star(x, y, get_color('white'), star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines
    trt.end_fill()


def draw_five_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        x = -206
        # create 5 stars in each row
        for star in range (0,5) :
            trt.fillcolor(get_color('white'))
            trt.begin_fill()
            draw_star(x, y, get_color('white'), star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines
    trt.end_fill()
    
def border():
    screen.bgcolor(get_color('white'))
    trt.color(get_color('black'))
    trt.penup()
    trt.setposition(-237,125)
    trt.pendown()
    trt.pensize(3)
    trt.forward(475)
    trt.rt(90)
    trt.forward(250)
    trt.rt(90)
    trt.forward(475)
    trt.rt(90)
    trt.forward(250)
    trt.hideturtle()

        
def main():
    draw_rectangle(start_x, start_y, flag_height, flag_length, get_color('white'))
    draw_stripes()
    draw_square()
    draw_six_stars_rows()
    draw_five_stars_rows()
    border()
    
if __name__ == "__main__":
    main()
trt.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()

