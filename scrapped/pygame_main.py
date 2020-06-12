#!/bin/python
import time
import sys

from pypygame import Window, Ring
from vec2d import Vec2d

colours = ['blue','magenta','red','orange','grey','white','yellow','green']

window = Window (size=(200,200))
ring = Ring (window,rinner=50,router=100)

#---------------------------------------------------------------------------------------------#
window.open ()
window.center_mouse ()

switch = True
while window.isopen:
    window.process_events ()

    mouse = Vec2d (window.mousepos)
    mouse -= window.centre
    mouse.angle += 90
    mouse.angle += 180 / ring.segments
    if mouse.angle < 0:
        angle = 360+mouse.angle
    else:
        angle = mouse.angle

    if mouse.length > ring.ri:
        segment = int (angle / (360 / ring.segments))
        ring.colour = colours[segment]
        switch = True
        time.sleep (0.1)

    #window.fill ()

    if switch:
        ring.draw ()
        window.update ()
        window.center_mouse ()
        switch = False
    time.sleep (0.03)

else:
    sys.exit ()
