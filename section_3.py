# Section_3
# camryn Echevarria
# 11/4/2022

# Section 1 is the beginning of the game that gives you 4 choices to pick from the game to keep going.
# import main_character and section_2 here

# This start function is called by main_game.
# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start(section_3):
    print("""1. Sugar land
2. Chocolate land
    Enter death or life""")

    option_section_1 = int(input("Which path do you like to take next?:"))

    if option_section_3 == 1:
        print("lose half live and all the rings while falling in sour juice river.")

    elif option_section_3 == 2:
        print("complete the level and now you on to the next level to help collect more ring and lives with sonic.")
        section_3.start()
    else:
        print("Incorrect input")





# Be sure to put their choice in a variable!

# Then use an if/elif/else statement to do something based on the player's choice.

# One of the options should move the story to the next section with code like this: section_1.start()


# Add pseudocode here to describe the rest of the functionality of this section of your game.
# You may also draw and submit flowcharts if you prefer.