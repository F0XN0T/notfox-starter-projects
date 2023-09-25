import random

def roll():
    min_roll = 1
    max_roll = 6
    dice_roll = random.randint(min_roll, max_roll)
    return dice_roll

while True:
    players = input("🐷 🎃 🌖Enter the number of players (2-4) or 'q' to quit: ")
    
    if players.lower() == 'q':
        print("🐷 🎃 🌖Quitting the game.")
        exit()
    
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("🐷 🎃 🌖Must be between 2 - 4 players")
    else:
        print("🐷 🎃 🌖Invalid player amount, try again (2-4) or 'q' to quit: ")

max_gorebites = 50
player_gorebites = [0 for _ in range(players)]

while True:
    for player_idx in range(players):
        if player_gorebites[player_idx] >= max_gorebites:
            continue  # Skip the turn for this player if they have already reached 50 or more
        print("🐷 🎃 🌖Player", player_idx + 1, "it's your turn\n")
        current_gorebites = 0

        while True:
            should_roll = input("🐷 🎃 🌖Enter 'r' to roll or 'q' to quit: ")
            if should_roll.lower() == 'q':
                print("🐷 🎃 🌖Quitting the game.")
                exit()
            elif should_roll.lower() != 'r':
                break

            value = roll()
            if value == 1:
                print("🐷 🎃 🌖Oh no, you rolled a 1! 🐷 🎃 🌖")
                current_gorebites = 0
                break
            else:
                current_gorebites += value
                print("🐷 🎃 🌖You rolled a:", value, "🐷 🎃 🌖")

            print("🐷 🎃 🌖You have", current_gorebites, "gorebites so far 🐷 🎃 🌖")

            if player_gorebites[player_idx] + current_gorebites >= max_gorebites:
                # Calculate the remaining points after reaching 50
                remaining_points = max_gorebites - player_gorebites[player_idx]
                current_gorebites = remaining_points  # Set current score to remaining points
                player_gorebites[player_idx] = max_gorebites  # Update player's total score
                print(f"🐷 🎃 🌖Player {player_idx + 1} has reached 50 or more and saved {remaining_points} gorebites.")
                break

        player_gorebites[player_idx] += current_gorebites
        print("🐷 🎃 🌖You have", current_gorebites, "gorebites in total 🐷 🎃 🌖")

    # Check if there are multiple players who have reached 50 or more
    winning_players = [i for i, score in enumerate(player_gorebites) if score >= max_gorebites]

    if len(winning_players) >= 2:
        print("🐷 🎃 🌖Multiple players have reached 50 or more. It's time for a 1v1 match!")
        # Continue the game in a 1v1 match until there is only one winner
        while len(winning_players) > 1:
            for player_idx in winning_players:
                if player_gorebites[player_idx] >= max_gorebites:
                    continue  # Skip the turn for this player if they have already reached 50 or more
                print("🐷 🎃 🌖Player", player_idx + 1, "it's your 1v1 turn\n")
                current_gorebites = 0

                while True:
                    should_roll = input("🐷 🎃 🌖Enter 'r' to roll or 'q' to quit: ")
                    if should_roll.lower() == 'q':
                        print("🐷 🎃 🌖Quitting the game.")
                        exit()
                    elif should_roll.lower() != 'r':
                        break

                    value = roll()
                    if value == 1:
                        print("🐷 🎃 🌖Oh no, you rolled a 1! 🐷 🎃 🌖")
                        current_gorebites = 0
                        break
                    else:
                        current_gorebites += value
                        print("🐷 🎃 🌖You rolled a:", value, "🐷 🎃 🌖")

                    print("🐷 🎃 🌖You have", current_gorebites, "gorebites so far 🐷 🎃 🌖")

                    if player_gorebites[player_idx] + current_gorebites >= max_gorebites:
                        # Calculate the remaining points after reaching 50
                        remaining_points = max_gorebites - player_gorebites[player_idx]
                        current_gorebites = remaining_points  # Set current score to remaining points
                        player_gorebites[player_idx] = max_gorebites  # Update player's total score
                        print(f"🐷 🎃 🌖Player {player_idx + 1} has reached 50 or more and saved {remaining_points} gorebites.")
                        break

                player_gorebites[player_idx] += current_gorebites
                print("🐷 🎃 🌖You have", current_gorebites, "gorebites in total 🐷 🎃 🌖")

                # Check if this player has won the 1v1 match
                if player_gorebites[player_idx] >= max_gorebites:
                    print(f"🐷 🎃 🌖Player {player_idx + 1} has won the 1v1 match!")
                    exit()

    # Check if there is a single player who has reached 50 or more to declare them as the winner
    if len(winning_players) == 1:
        winner = winning_players[0]
        print(f"🐷 🎃 🌖Player {winner + 1} has reached or exceeded 50 gorebites and wins! The game is over.")
        exit()
