# scripts/flow_common.rpy

label prologue_start:
    scene bg room
    show eileen happy at center

    e "Welcome to the boilerplate setup."
    e "This is the 'Common Route'. Your choices here matter."

    menu:
        "I prefer lasers and robots.":
            $ player.scifi_points += 1
            e "A futurist, I see."
        "I prefer magic and dragons.":
            $ player.fantasy_points += 1
            e "A classicist! Nice."

    e "Now, the story must branch."

    # --- THE CRITICAL BRANCH ---
    menu:
        "Enter the Sci-Fi Timeline":
            $ route_locked = "scifi"
            jump route_a_ch1
        
        "Enter the Fantasy Timeline":
            $ route_locked = "fantasy"
            jump route_b_ch1