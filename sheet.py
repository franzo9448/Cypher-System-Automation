# Define the stats and their corresponding Pools and Edges
stats = {}
xp = 0
purchased_options=0
tier =0

# Define a function to set the stats and their Pools and Edges
def set_stats():
    global stats
    print("Enter your stats and their corresponding Pools and Edges (e.g. 'Might: 12, 2')")
    for stat in ["Might", "Speed", "Intellect"]:
        input_str = input(f"{stat}: ")
        stat_values = input_str.split(", ")
        stats[stat] = (int(stat_values[0]), int(stat_values[1]))
    print(f"Stats set: {stats}")


# Define a function to apply Effort to a task
def apply_effort(stat, effort_level):
    """
       Applies effort to a task using a specified number of points from a given stat pool.
       Args:
           stat (str): The stat to use for applying effort.
           effort_level (int, optional): The number of levels of effort to apply. Default is 1.
       """
    stat_pool = stats[stat][0]
    if stat_pool < effort_level * 3:
        print(f"Error: Not enough points in the {stat} Pool to apply {effort_level} levels of Effort")
        return

    # Reduce the difficulty of the task by one step for each level of Effort applied
    difficulty_modifier = -1 * effort_level
    print(
        f"Successfully applied {effort_level} levels of Effort to the task using {effort_level * 3} points from the {stat} Pool")
    stats[stat] = (stat_pool - (effort_level * 3), stats[stat][1])

# Define a function to increase the character's capabilities
def increase_capabilities(point_amount):
  """
    Increases the character's capabilities by adding points to their stat pools.
    Args:
        point_amount (int): The number of points to add to each stat pool.
"""
  global stats
  for stat in ["Might", "Speed", "Intellect"]:
    input_str = input(f"Enter the number of points to add to the {stat} Pool: ")
    points_to_add = int(input_str)
    stat_pool = stats[stat][0]
    stats[stat] = (stat_pool + points_to_add, stats[stat][1])
  print(f"Capabilities increased: {stats}")

def improve_edge():
        """
        Improves the edge for a specified stat.
        """
        global stats
        print("Enter the stat to improve the Edge for (Might, Speed, or Intellect)")
        stat = input()
        stat_edge = stats[stat][1]
        stats[stat] = (stats[stat][0], stat_edge + 1)
        print(f"{stat} Edge improved: {stats[stat]}")

def recover_points(stat):
    """
        Recovers points for a specified stat pool.
        Args:
            stat (str): The stat to recover points for.
"""
    global stats
    print(f"Enter the number of points to recover for the {stat} Pool:")
    input_str = input()
    points_to_recover = int(input_str)
    stat_pool = stats[stat][0]
    stats[stat] = (stat_pool + points_to_recover, stats[stat][1])
    print(f"Points recovered for the {stat} Pool: {stats[stat]}")

def purchase_special_option():
  global xp
  global purchased_options
  print("Enter the number of the special option you want to purchase:")
  print("1. Reduce the cost for wearing armor")
  print("2. Add 2 to your recovery rolls")
  print("3. Select a new type-based ability from your tier or a lower tier")
  input_str = input()
  option_number = int(input_str)
  if option_number == 1:
    print("Successfully purchased the option to reduce the cost for wearing armor")
  elif option_number == 2:
    print("Successfully purchased the option to add 2 to your recovery rolls")
  elif option_number == 3:
    print("Successfully purchased the option to select a new type-based ability from your tier or a lower tier")
  else:
    print("Invalid option number")
    return
  xp -= 4
  print(f"XP remaining: {xp}")
  purchased_options += 1
  if purchased_options == 4:
    print("You have purchased 4 options and can advance to the next tier!")

def print_tier_and_xp():
  global xp
  global tier
  print(f"Current tier: {tier}")
  print(f"XP: {xp}")

def create_character_sheet():
    """
    Creates a character sheet for a character and saves it to a text file.
    """
    global stats
    global xp
    global purchased_options
    global tier

    # Set the character's stats
    set_stats()

    # Apply effort to a task
    apply_effort("Might", 2)

    # Increase the character's capabilities
    increase_capabilities(3)

    # Improve the edge for a specified stat
    improve_edge()

    # Recover points for a specified stat pool
    recover_points("Intellect")

    # Purchase a special option
    purchase_special_option()

    # Print the current tier and XP
    print_tier_and_xp()

    # Save the character sheet to a text file
    with open("character_sheet.txt", "w") as f:
        f.write(f"Stats: {stats}\n")
        f.write(f"XP: {xp}\n")
        f.write(f"Purchased options: {purchased_options}\n")
        f.write(f"Tier: {tier}\n")


def menu():
    """
    Displays a menu of options and calls the corresponding functions.
    """
    global stats
    global xp
    global purchased_options
    global tier

    while True:
        print("\nMenu:")
        print("1. Set stats")
        print("2. Apply effort to a task")
        print("3. Increase capabilities")
        print("4. Improve edge")
        print("5. Recover points")
        print("6. Purchase special option")
        print("7. Print current tier and XP")
        print("8. Create character sheet and save to text file")
        print("9. Quit")
        input_str = input("Enter the number of the option you want to choose: ")
        option = int(input_str)

        if option == 1:
            set_stats()
        elif option == 2:
            print("Enter the stat to use for applying effort (Might, Speed, or Intellect)")
            stat = input()
            print("Enter the number of levels of effort to apply (1, 2, or 3)")
            input_str = input()
            effort_level = int(input_str)
            apply_effort(stat, effort_level)
        elif option == 3:
            print("Enter the number of points to add to each stat pool")
            input_str = input()
            point_amount = int(input_str)
            increase_capabilities(point_amount)
        elif option == 4:
            improve_edge()
        elif option == 5:
            print("Enter the stat to recover points for (Might, Speed, or Intellect)")
            stat = input()
            recover_points(stat)
        elif option == 6:
            purchase_special_option()
        elif option == 7:
            print_tier_and_xp()
        elif option == 8:
            create_character_sheet()
        elif option == 9:
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)