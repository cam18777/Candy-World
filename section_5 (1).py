# section_5
# camryn echevarria
# 12/11/2022

def start():
    print("Made it to Gummy land where its sonic last chances to win after beating King Candy.")
    print("Now you have to beat the King Candy to win this level and finish the game.")
    print("Sonic is rolling fast and is quickly coming to the 100,000 rings")

    section_5 = input("""1. blow king up.
2. animals fight king for me
3. candy corn jail""")

    if section_5 == 1:
        print("blow King up.")
    elif section_5 == 2:
        print("animals fights King for me.")
    elif section_5 == 3:
        print("Candy corn jail traps king.")
    else:
        print("lost the game and has to start all over.")
        print("""King Candy started attacking. Candy hits me and took some damages.""")
