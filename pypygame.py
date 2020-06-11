# FIXME replace pygame dependency
# Should contain all the code that has to be replaced when replacing pygame.
import pygame
import math

colour = pygame.color.THECOLORS

class Window:
    isopen = True

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

    def process_events (self):
        for e in pygame.event.get ():
            if e.type == pygame.QUIT:
                self.isopen = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.isopen = False

    def center_mouse (self):
        pygame.mouse.set_pos (self.centre)

    @property
    def mousepos (self):
        return pygame.mouse.get_pos ()

    def close (self):
        pygame.quit ()

class Ring:

    def __init__ (self,window,rinner,router,segments=8):
        self.window = window
        self.ri = rinner
        self.ro = router
        self.segments = segments
        self.colour = 'white'

    def draw (self):
        pygame.draw.circle (self.window.surface,colour[self.colour],self.window.centre,self.ro,1)
        pygame.draw.circle (self.window.surface,colour[self.colour],self.window.centre,self.ri,1)

        # draw lines
        for i in range (self.segments):
            rad = math.radians (360 / self.segments * i + 180 / self.segments)
            cos,sin = math.cos (rad),math.sin (rad)
            pygame.draw.line (
                    self.window.surface,colour[self.colour],
                    (self.ro * cos + self.window.centre[0],self.ro * sin + self.window.centre[1]),
                    (self.ri * cos + self.window.centre[0],self.ri * sin + self.window.centre[1]),
                    1)

    def left_inner (self):
        ...
