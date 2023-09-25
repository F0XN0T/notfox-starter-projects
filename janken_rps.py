import random

player_wins = 0
npc_wins = 0

choices = ["guu", "paa", "choki"]

while True:
    player_input = input("Type 'guu' for rock, 'paa' for paper, 'choki' for scissors or 'q' to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in choices:
        continue

    random_number = random.randint(0, 2)
    # 0 is rock (guu) 1 is paper (paa) 2 is scissors (choki)
    npc_pick = choices[random_number]
    print("the npc choosed", npc_pick + ".")

    if player_input == "guu" and npc_pick == "choki":
        print("Anata wa kachimashita 🎉")
        player_wins += 1
        continue
    elif player_input == "paa" and npc_pick == "guu":
        print("Anata wa kachimashita 🎉")
        player_wins += 1
    elif player_input == "choki" and npc_pick == "paa":
        print("Anata wa kachimashita 🎉")
        player_wins += 1
    else:
        print("Anata wa makemashita 😭")
        npc_wins += 1

print("Anata wa", player_wins, "kachimashita.")
print("NPC wa", npc_wins, "kachimashita.")
print("Sayōnara")