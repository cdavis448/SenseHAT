from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
w = (255,255,255)
r = (255,0,0)
b = (0,0,255)
g = (0,255,0)
p = (255,0,255)
t = (0,255,255)
o = (160,82,45)
b = (165,42,42)
slug = [[2,4]]
trail = [[1,4],[1,4],[1,4],[1,4]]
direction = "up"
blank = (0,0,0)
vegan=[]
score = 0
pause = 0.15
dead = True
breed = 0
lastmove = "up"

# Functions ---------------------------
def draw_slug():
    for i in slug:
        sense.set_pixel(i[0],i[1],w)
def move():
    global score
    global pause
    global dead
    global direction
    global lastmove
    remove = True
    
    
    while True:
        if dead == True:   
            last = slug[-1]
            first = slug[0]
            next = list(last)
            
            if direction == "middle":
                if lastmove == "right":
                    lastmove = "right"
                    if last[0] + 1 == 8:
                        next[0] = 0
                    else:
                        next[0] = last[0] + 1
                elif lastmove == "left":
                    lastmove = "left"
                    if last[0] - 1 == -1:
                        next[0] = 7
                    else:
                        next[0] = last[0] - 1
                elif lastmove == "down":
                    lastmove = "down"
                    if last[1] + 1 == 8:
                        next[1] = 0
                    else:
                        next[1] = last[1] + 1
                elif lastmove == "up":
                    lastmove = "up"
                    if last[1] - 1 == -1:
                        next[1] = 7
                    else:
                        next[1] = last[1] - 1
            elif direction == "right":
                lastmove = "right"
                if last[0] + 1 == 8:
                    next[0] = 0
                else:
                    next[0] = last[0] + 1
            elif direction == "left":
                lastmove = "left"
                if last[0] - 1 == -1:

                    next[0] = 7
                else:
                    next[0] = last[0] - 1
            elif direction == "down":
                lastmove = "down"
                if last[1] + 1 == 8:
                    next[1] = 0
                else:
                    next[1] = last[1] + 1
            elif direction == "up":
                lastmove = "up"
                if last[1] - 1 == -1:
                    next[1] = 7
                else:
                    next[1] = last[1] - 1
            
            if next in slug:
                dead = False
            slug.append(next)
            sense.set_pixel(next[0], next[1], w)
            if remove == True:
                sense.set_pixel(first[0], first[1], blank)
                slug.remove(first)
            draw_slug()
        
            
            if [next[0],next[1]] in vegan:
                vegan.remove([next[0],next[1]])
                score = score + 1
                if score % 5 == 0:
                    remove = False
                elif score % 10 == 0:
                    if pause >= 0.10:
                        pause = pause - 0.01
            else:
                remove = True
            sleep(pause)
            if len(vegan) < 5:
                make_veg()
        else:
            sense.show_message(str(score) + " points")
        lastmove = direction
def joystick_moved(event):
    global direction
    direction = event.direction
def make_veg():
    global breed
    breed = randint(0,6)
    if randint(1,10) / 10 > 7/10:
        x = randint(0,7)
        y = randint(0,7)
        food = [x,y]
        if food in slug or vegan:
            if len(vegan) < 5:
                x = randint(0,7)
                y = randint(0,7)
        if breed == 0:
            sense.set_pixel(x,y,b)
        elif breed == 1:
            sense.set_pixel(x,y,g)
        elif breed == 2:
            sense.set_pixel(x,y,p)
        elif breed == 3:
            sense.set_pixel(x,y,t)
        elif breed == 4:
            sense.set_pixel(x,y,o)
        elif breed == 5:
            sense.set_pixel(x,y,b)
        else:
            sense.set_pixel(x,y,r)     
        vegan.append([x,y])

# Main program ------------------------
sense.clear()
draw_slug
sleep(0.1)
sense.stick.direction_any = joystick_moved
move()

