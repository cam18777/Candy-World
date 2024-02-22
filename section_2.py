# Section_2
# camryn Echevarria
# 11/4/2022

# Section 1 is the beginning of the game that gives you 4 choices to pick from the game to keep going.
# import main_character and section_2 here

# This start function is called by main_game.
# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start(section_2):
    print("Sonic finds the right path that he needs to take to collect all his shiny rings.")

    print("Sonic is Now realizing what the next path is to take to keep winning.")

    print("Now sonic has less Chance to pick the right path to Survive the game.")

    print("What the next path that you like take your chances on next to Survive?:")

    option_section_2 = int(input("""1. Sugar land
2. chocolate land
3. gummy land
Enter death or life here
"""))
    if option_section_2 == 1:
        print("lose half lives while falling into sour juice river.")
    elif option_section_2 == 2:
        print("lose half live while falling into nesquik sand.")
    elif option_section_2 == 3:
        print("completed the level and keep going to collecting more rings to help sonic stay alive and win the game.")
        section_3.start()
    else:
        print("Incorrect input")


# Then use an if/elif/else statement to do something based on the player's choice.

# One of the options should move the story to the next section with code like this: section_1.start()


 # Add pseudocode here to describe the rest of the functionality of this section of your game.
# You may also draw and submit flowcharts if you prefer.
