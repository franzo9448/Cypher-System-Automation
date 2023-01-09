races = {
    "Dwarf": {
        "Darkvision": "You have better perception in the dark than most. You are specialized in low-light spotting. Enabler.",
        "Dwarven Resilience": "You gain an asset for Might defense rolls against poisons and toxins. Enabler.",
        "Dwarven Combat Training": "You are practiced with the battleaxe, handaxe, throwing hammer, and warhammer. Enabler.",
        "Underground": "You have spent much of your life in mines and caverns. You gain an asset to Survival and Perception rolls when underground. You are trained in tasks related to stone, including sensing stonework traps, knowing the history of stonecraft, and knowing your distance beneath the surface. Enabler.",
    },
    "Elf": {
        "Low-Light Vision": "You have better perception in the dark than many. You are trained in low-light spotting. Enabler.",
        "Keen Senses": "You are trained in Perception. Enabler.",
        "Follow Ancestry": "You gain an asset to Intellect defense rolls against being charmed, and magic can't put you to sleep. You do not need to sleep, but instead, enter a trance for 8 hours. Enabler.",
        "Elven Weapon Training": "You are practiced with the longsword, shortsword, shortbow, and longbow. Enabler.",
    },
    "Gnome": {
        "Darkvision": "You have better perception in the dark than most. You are specialized in low-light spotting. Enabler.",
        "Underground": "You have spent much of your life in mines and caverns. You gain an asset to Survival and Perception rolls when underground. Enabler.",
        "Gnome Cunning": "You gain an asset for all defense rolls to resist magic. Enabler.",
        "Artificer's Lore": "You are trained in Intellect tasks related to magic items, alchemical objects, or technological devices. Enabler.",
    },
    "Halfling": {
        "Brave": "You gain an asset for Intellect defense tasks against being frightened. Enabler.",
        "Halfling Nimbleness": "You can move through the space of any creature that is of a size larger than yours. Enabler.",
        "Halfling Combat Training": "You are practiced with daggers, short swords, and slings. Enabler.",
        "Naturally Stealthy": "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you. Enabler.",
    },
    "Human": {
        "Pool Points": "Add 4 points to any one pool.",
        "Improved Edge": "Choose one of your Edge stats that is 0. It increases to 1. Enabler.",
        "Skilled": "Choose any two skills you are untrained in. You are trained in those two skills. Enabler.",
    },
    "Celestial": {
        "Darkvision": "You have better perception in the dark than most. You are specialized in low-light spotting. Enabler.",
        "Celestial Resistance": "You have Armor 2 against necrotic damage or other types of evil damage. Enabler.",
        "Healing Hands": "As an action, you can touch another creature and cause it to gain a free recovery roll. You can use this ability once per day for every character tier. Action."
    },
    "Draconic": {
        "Draconic Heritage": "Choose a draconic heritage, such as red, black, green, blue, white, gold, brass, copper, silver, bronze, or another gameworld-specific type. You have an associated damage type that affects your other abilities, such as fire, acid, poison, lightning, cold, or another gameworld-specific type. Enabler.",
        "Intimidating": "You have an asset to Intimidation skill checks. Enabler.",
        "Draconic Resistance": "You gain Armor 2 against the type of energy associated with your draconic heritage. Enabler.",
        "Dragonbreath": "As an action, you breathe out a blast of energy related to your draconic heritage in a 10-foot cone (immediate distance). The blast inflicts 3 points of damage of this kind of energy (ignores Armor) to all creatures or objects within the area. For every level of Effort, add two points to the damage. Once you use this trait, you can't use it again until you rest at least 10 hours. Action."
    },
}
def print_race_info(race):
    """
    Prints the attributes of a specific race.
    Args:
        race (str): The name of the race.
    """
    if race in races:
        for attribute, description in races[race].items():
            print(f"{attribute}: {description}")
    else:
        print("Race not found")

