#!/bin/python
import time
import pygame
import sys
import math

def process_events ():
    keepopen = True
    for e in pygame.event.get ():
        if e.type == pygame.QUIT:
            keepopen = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            keepopen = False
    return keepopen

class Window:

    def __init__ (self,size):
        self.width = size[0]
        self.height = size[1]

    def open (self):
        pygame.init ()
        self.surface = pygame.display.set_mode (self.size)

    @property
    def size (self):
        return self.width,self.height

    @property
    def centre (self):
        return int (self.width/2),int (self.height/2)

    def fill (self,colour=(0,0,0)):
        self.surface.fill (colour)

    def update (self):
        pygame.display.flip ()

    def draw (self,object_):
        object_.draw (self.surface,*self.centre)

class Circle:

    def __init__ (self,ri,ro,segments=8):
        self.ri = ri
        self.ro = ro
        self.segments = segments
        self.colour = (222,222,222)

    def draw (self,surface,x=0,y=0):
        pygame.draw.circle (surface,self.colour,(x,y),self.ro,1)
        pygame.draw.circle (surface,self.colour,(x,y),self.ri,1)

        for i in range (self.segments):
            rad = math.radians (360 / self.segments * i+22.5)
            cos_,sin_ = math.cos (rad),math.sin (rad)
            xa = self.ro * cos_ + x
            ya = self.ro * sin_ + y
            xb = self.ri * cos_ + x
            yb = self.ri * sin_ + y
            pygame.draw.line (surface,self.colour,(xa,ya),(xb,yb),1)

colours = ['blue','magenta','red','orange','grey','white','yellow','green']

window = Window (size=(200,200))
circle = Circle (50,100)

window.open ()
pygame.mouse.set_pos (window.centre)

switched = False
keepopen = True
while keepopen:
    keepopen = process_events ()
    mousex,mousey = pygame.mouse.get_pos ()
    mousex,mousey = mousex-window.width/2,mousey-window.height/2
    if math.sqrt (mousex**2 + mousey**2) > circle.ri:
        deg = math.degrees (math.atan2 (mousex,mousey))
        c = colours[int ((deg - (180 / circle.segments))/ (360 / circle.segments))]
        circle.colour = pygame.color.THECOLORS[c]
        time.sleep (0.5)
        switched = True

    window.fill ()
    window.draw (circle)
    window.update ()
    if switched:
        pygame.mouse.set_pos (window.centre)
        switched = False

else:
    pygame.quit ()
    sys.exit ()
