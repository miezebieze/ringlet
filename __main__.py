from enum import Enum
from window import Window

D = Enum ('Directions','N NE E SE S SW W NW')

selector_map = {
        D.NW: [0.5,0.5], D.N: [1.5,0], D.NE: [2.5,0.5],
        D.W: [0,1.5],                    D.E: [3,1.5],
        D.SW: [0.5,2.5], D.S: [1.5,3], D.SE: [2.5,2.5],
        }

selector_size = 100
window_size = selector_size*4

window = Window (window_size,window_size,selector_map,selector_size,selector_size)

# set actions here
from functools import partial
def say (something):
    print (''.join (('Me: "',something,'"')))

window.actions[D.NW] = partial (say,'northwast')
window.actions[D.N] = partial (say,'north')
window.actions[D.NE] = partial (say,'neorthest')
window.actions[D.W] = partial (say,'western')
window.actions[D.E] = partial (say,'easy')
window.actions[D.SW] = partial (say,'suess whest')
window.actions[D.S] = partial (say,'sissy')
window.actions[D.SE] = partial (say,'seoul')

window.go ()
