from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
w = (255,255,255)
r = (255,0,0)
slug = [[2,4],[3,4],[4,4]]
direction = "right"
blank = (0,0,0)
vegan=[]
score = 0
# Functions ---------------------------
def draw_slug():
    for i in slug:
        sense.set_pixel(i[0],i[1],w)
def move():
    global score
    remove = True
    while True:
        if len(vegan) < 5:
            make_veg()
        last = slug[-1]
        first = slug[0]
        next = list(last)
        if direction == "right":
            if last[0] + 1 == 8:
                next[0] = 0
            else:
                next[0] = last[0] + 1
        elif direction == "left":
            if last[0] - 1 == -1:

                next[0] = 7
            else:
                next[0] = last[0] - 1
        elif direction == "down":
            if last[1] + 1 == 8:
                next[1] = 0
            else:
                next[1] = last[1] + 1
        elif direction == "up":
            if last[1] - 1 == -1:
                next[1] = 7
            else:
                next[1] = last[1] - 1
        slug.append(next)
        sense.set_pixel(next[0], next[1], w)
        if remove == True:
            sense.set_pixel(first[0], first[1], blank)
            slug.remove(first)
        draw_slug()
        
        if [next[0],next[1]] in vegan:
            vegan.remove([next[0],next[1]])
            score = score + 1
            if score % 2 == 0:
                remove = False
            else:
                remove = True
        sleep(0.15)
def joystick_moved(event):
    global direction
    direction = event.direction
def make_veg():
    x = randint(0,7)
    y = randint(0,7)
    while [x,y] in slug:
        x = randint(0,7)
        y = randint(0,7)
        sense.set_pixel(x,y,r)
    vegan.append([x,y])

# Main program ------------------------
sense.clear()
draw_slug
sleep(0.1)
sense.stick.direction_any = joystick_moved
move()
make_veg()
move()

