# scott-launcher

Excuse this jumbled mess. I'm just trying to create the next major generation of graphical interfaces.

inspiration
---
THE GUI SHOULD BE A LOT BETTER by Scott Ross
https://www.youtube.com/watch?v=AItTqnTsVjA&t=3940

design
---
After launching the program, a ring shows up around the cursor.
The ring is split into at most eight segments, each being associated with a child node.
When the cursor is moved over a segment, the cursor is reset to it's original position and the
child node is opened. When the child node contains more child nodes, these extend into the ring view.
When the child was an end node, some action is executed or when it was directory node, the directory
view is opened.

The basic view:
    The eight items can be changed.
        When empty, the creation menu is shown after clicking the segment.
        When occupied, the item opens a new view.
The file view:
    The files are organized in a circular fashion.
    The names are shown in half circles around them
    Pointing at items shows their full name in a tool tip.
    Files and directories are opened by left clicking.
    Right clicking on items shows the context ring.

The monitor:
    Holding a button makes the monitor appear around the cursor.
    It shows hardware resources and the systray.
