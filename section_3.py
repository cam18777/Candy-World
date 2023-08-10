# Section_3
# camryn Echevarria
# 11/4/2022
# Section_3
# camryn Echevarria
# 11/4/2022

import section_4


def start():
    while True:
        print("""1. Sugar land
2. Chocolate land
    Enter death or life""")

        section_3 = int(input("Which path do you like to take next?:"))

        if section_3 == 1:
            print("lose half live and all the rings while falling in sour juice river.")

        elif section_3 == 2:
            print("complete the level and now you on to the next level to help collect more ring and lives with sonic.")
            section_4.start()
        else:
            print("Incorrect input")


# start()
