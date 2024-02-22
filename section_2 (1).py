# Section_2
# camryn Echevarria
# 11/4/2022

import section_3

def start():

    print("Sonic finds the right path that he needs to take to collect all his shiny rings.")

    print("Sonic is Now realizing what the next path is to take to keep winning.")

    print("Now sonic has less Chance to pick the right path to Survive the game.")

    print("What the next path that you like take your chances on next to Survive?:")

    while True:
        print("""1. Sugar land
2. chocolate land
3. gummy land""")

        option_section_2 = int(input("Pick next path?"))
        if option_section_2 == 1:
            print("lose half lives while falling into sour juice river.")
        elif option_section_2 == 2:
            print("lose half live while falling into nesquik sand.")
        elif option_section_2 == 3:
            print("completed the level and keep going to collecting more rings to help sonic stay alive and win the game.")
            section_3.start()
        else:
            print("Incorrect input")

# start()
