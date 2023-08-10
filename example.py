import section_2


# Section 1 is the beginning of the game that gives you 4 choices to pick from the game to keep going.
# import main_character and section_2 here


# intro to the first part
def start():
    print("""Infinite path of sour strips on a bright cotton candy day when sonic is unable to pick the path.
To help sonic find all the rings that will help him complete the adventure.""")

print("""Sonic is seeking the right path to collect as many rings as possible to win the game.
Sonic has full health and does not know what path to take to start his journey.
While sonic on his crazy adventure that sonic encounters a big decision of witch path to take.""")

# sonic picks
print("""1. Sugar land
2. Bubble gum land
3. Chocolate land
 4. Gummy land""")

option_section_1 = int(input("Which path do you like to take first?:"))

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