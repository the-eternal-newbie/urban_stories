label route_b_ch1:
    show eileen neutral

    if player.scifi_points > 0:
        e "I knew you'd pick this one. You showed interest earlier."
    else:
        e "Surprised you picked this one, given your earlier answers."

    # Example of scaling logic
    "You find a laser pistol."
    $ player.add_item("Laser Pistol")
    
    "[player.inventory]"

    return