# Section_4
# camryn Echevarria
# 11/6/2022

# Section 1 is the beginning of the game that gives you 4 choices to pick from the game to keep going.
# import main_character and section_2 here

# This start function is called by main_game.
# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start(section_4):
    print("Onto the last path that he thinks he can find his last amount rings on the path to win the game.")
    print("What the next path that you like to try next to stay live and beet all the Booby traps?")

    # print("""write the beginning of you story here and delete the # when done""")
    # print("""write the beginning of you story here and delete the # when done""")
    print("""1. Sugar land
Enter death or life here""")

    option_section_4 = int(input("Which path do you like to take?:"))

    if option_section_4 == 1:
        print("complete the level and now you on to the next level to help collect more ring and lives with sonic.")
        section_5.start()
    else:
        print("Incorrect input")


# Be sure to put their choice in a variable!
# Then use an if/elif/else statement to do something based on the player's choice.

# One of the options should move the story to the next section with code like this: section_1.start()


# Add pseudocode here to describe the rest of the functionality of this section of your game.
