design (wip)
---
After launching the program, a ring shows up around the cursor.
The ring is split into at most eight segments,
  each being associated with a child node.
When the cursor is moved over a segment, the cursor is reset to
  the center and the child node is opened.
  If the child node contains more child nodes, these extend into
    a new ring view.
  If the child was an end node, some action is executed.
  If it's empty, the node creator is started.

The basic view:
  The eight items can be changed.
    When empty, the creation menu is shown after
    clicking the segment.
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

files
---
/bin/ringlet
/lib/pythonx.x/site-packages/ringlet/
    The main program which only contains the front end and a simple demo.
    For Windows maybe a zipapp would be feasable.
/bin/ringlet-launcher
    This checks the application that currently is focused and opens ringlet with the ring that's
    configured for that app or the default.
/usr/share/ringlet/rings/
$HOME/.local/share/ringlet/rings/
    The rings need a json file that specifies titles, icons, placement and actions.
    A ring can have it's own directory for easy drop in of user made rings.
/usr/share/ringlet/extensions/
$HOME/.local/share/ringlet/extensions/
    Extensions are placed in a directory in the apps config.
    The extensions dir has an __init__.py .
    A package manager is used to de-/activate them by editing the __init__.py .
    When an extension has multiple files, it has it's own directory with an __init__.py .
/etc/ringlet/rc.json (base config)
$HOME/.config/ringlet/rc.json (user config)
    The rc file contains global options for all rings.

extensions
---
Extensions are written in python.
