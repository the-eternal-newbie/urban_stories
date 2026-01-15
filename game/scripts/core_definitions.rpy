# 00_definitions.rpy

# 1. Characters
# Use short variables for scripting speed, define colors for clarity.
define e = Character("Eileen", color="#c8ffc8")

# 2. Images (Optional if you use the 'images' folder correctly, but good for specific tweaks)
# RenPy auto-defines 'images/bg/classroom.png' as "bg classroom" automatically.

# 3. Transforms (Animations)
transform slight_nod:
    yoffset 0
    linear 0.1 yoffset 10
    linear 0.1 yoffset 0