# 01_state.rpy

# --- Python Logic for Complex State ---
init python:
    class PlayerState:
        def __init__(self):
            self.scifi_points = 0
            self.fantasy_points = 0
            self.karma = 0
            self.inventory = []

        def add_item(self, item):
            if item not in self.inventory:
                self.inventory.append(item)

# --- RenPy Variables ---
# 'default' initializes data. It ensures variables exist in save files.
# DO NOT put these in a label.

default player = PlayerState() # Initialize our python object
default current_chapter = 0
default route_locked = None    # "scifi or fantasy", "bad route" or "good route" etc.