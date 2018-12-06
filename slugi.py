from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
w = (255,255,255)
slug = [[2,4],[3,4],[4,4]]
direction = "right"
blank = (0,0,0)
# Functions ---------------------------
def draw_slug():
    for i in slug:
        sense.set_pixel(i[0],i[1],w)
def move():
    while True:
        last = slug[-1]
        first = slug[0]
        next = list(last)
        if direction == "right":
            if last[0] + 1 == 8:
                next[0] = 0
            else:
                next[0] = last[0] + 1
        slug.append(next)
        sense.set_pixel(next[0], next[1], w)
        sense.set_pixel(first[0], first[1], blank)
        slug.remove(first)
        draw_slug()
        sleep(0.3)
# Main program ------------------------
sense.clear()
draw_slug
sleep(0.1)
move()

