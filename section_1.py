# Section_1
# camryn Echevarria
# 11/4/2022
import section_2


# Section 1 is the beginning of the game that gives you 4 choices to pick from the game to keep going.
# import main_character and section_2 here

# This start function is called by main_game.
# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start(section_1):
    # print("""write the beginning of you story here and delete the # when done""")
    # print("""write the beginning of you story here and delete the # when done""")
    print("""1. Sugar land
2. Bubble gum land
3. Chocolate land
4. Gummy land
""")

    option_section_1 = int(input("Which path do you like to take?:"))

    if option_section_1 == 1:
        print("lose half live and all the rings while falling in sour juice river.")

    elif option_section_1 == 2:
        print("complete the level and now you on to the next level to help collect more ring and lives with sonic.")
        section_2.start()

    elif option_section_1 == 3:
        print("lose half live and all the rings while falling in Nesquik sand.")

    elif option_section_1 == 4:
        print("lose half live and all the rings while getting tied up by licorice.")

    else:
        print("Incorrect input")

        # Be sure to put their choice in a variable!

        # Then use an if/elif/else statement to do something based on the player's choice.

        # One of the options should move the story to the next section with code like this:

        # Add pseudocode here to describe the rest of the functionality of this section of your game.
        # You may also draw and submit flowcharts if you prefer.
