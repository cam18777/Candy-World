# Section_5
# camryn Echevarria
# 11/6/2022

# Section 1 is the beginning of the game that gives you 4 choices to pick from the game to keep going.
# import main_character and section_2 here

# This start function is called by main_game.
# This will control the whole section.
# It'll need the player character as an input in order to interact with them.
def start(section_5):
    print("Made it to Gummy land where its sonic last chances to win agter beating King Candy.")
    print("Now you have to beat the King Candy to win this level and finish the game.")
    print("Sonic is rolling fast and is quickly coming to the 100,000 rings")
    
    print("Here the last path you will take to keep the game going and to win:")
    print("pick one move to use to beat King Candy.")
    
    option_section_5 = int(input("""1. throw gumballs bombs
    2. animals crackers
    3. Candy corn trap
    Enter fighting weapon to use"""))
    
    if option_section_5 == 1:
        print("blow King up.")
    elif option_section_5 == 2:
        print("animals fights King for me.")
    elif option_section_5 == 3:
        print("Candy corn jail traps king.")
    else:
        print("lost the game and has to start all over.")



    # Be sure to put their choice in a variable!

    # Then use an if/elif/else statement to do something based on the player's choice.

    # One of the options should move the story to the next section with code like this: section_1.start()


    # Add pseudocode here to describe the rest of the functionality of this section of your game.
    # You may also draw and submit flowcharts if you prefer.