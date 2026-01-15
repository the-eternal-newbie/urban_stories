# Purpose: The Main Loop. It should act as a traffic controller, not the story itself.

# The script of the game goes in this file.
# Declarations were moved to scripts/core_defiinitions

# The game starts here.

label start:
    # 1. Setup (if needed)
    $ current_chapter = 1

    # 2. Start the (common) flow 
    jump prologue_start

    # 3. Failsafe (Game should never reach here ideally)
    return
