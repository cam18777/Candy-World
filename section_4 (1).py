# Section_4
# camryn Echevarria
# 11/6/2022

import section_5


def start():
    print("On to the last path that he thinks he can find his last amount of rings on the path to win the game.")
    print("Here the last path that you like to try next to stay live and beet the Booby traps?")

    print("""1. Sugar land Enter 1 for your final path.""")
    path_choice = False
    while not path_choice:
        path_choice = int(input("Which path do you like to take?:"))
        if path_choice == 1:
            print("complete the level and now you on to the next level to help collect more ring and lives with sonic.")
            path_choice = True
            section_5.start()
        else:
            print("Incorrect input")
