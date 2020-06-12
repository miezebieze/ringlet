import Xlib
import Xlib.display
from Xlib import X

import time

def nop ():
    ...

class Window (object):

    def __init__ (self,width,height,selector_map,selector_width,selector_height):
        self.display = Xlib.display.Display ()
        self.screen = self.display.screen ()

        # FIXME place window under cursor
        x,y = 100,100
        self.root = self.screen.root.create_window (
                x, y, width, height, border_width=0,
                depth=self.screen.root_depth,
                event_mask=X.ExposureMask)
        self.root.set_wm_class ('ringlet','ringlet')

        self.actions = {sel:nop for sel in selector_map}

        self.selectors = {
                sel:self.root.create_window (
                    x=int (map_[0]*selector_width), y=int (map_[1]*selector_height),
                    width=selector_width, height=selector_height,
                    border_width=0, depth=self.screen.root_depth,
                    background_pixel=self.screen.white_pixel,
                    event_mask=X.ExposureMask|X.KeyPressMask|X.PointerMotionMask)
                for sel,map_ in selector_map.items ()}


    def go (self):
        self.root.map ()
        [sel.map () for sel in self.selectors.values ()]

        while True:
            t = time.time ()
            e = self.display.next_event ()

            if e.type == X.MotionNotify:
                for d,win in self.selectors.items ():
                    if win == e.window:
                        self.actions[d] ()

