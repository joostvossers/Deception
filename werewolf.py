"""
    Deception Detection in the Werewolf Game
    Trends in Interactive Intelligent Environments (5DV210) at Umeå University, 2023.
    Fanny Danelid, fada0025
    Joost Vossers, joge0053
"""
import json
import numpy as np

# ==================== Initialisation ====================
# Ask for input files:
game_file_name = input("Please provide the filename containing the game input\n")
trust_file_name = input("Please provide the filename containing the reasoning input\n")

# Open and read the game file:
game_file_path = "input/" + game_file_name
game_file = open(game_file_path)
game_data = json.load(game_file)

# Open and read the trust file:
trust_file_path = "input/" + trust_file_name
trust_file = open(trust_file_path)
trust_data = json.load(trust_file)

# Initialise trust values at 0.5:
trust = {}
players = game_data["day 1"]["arguments"]
for p in players:
    trust[p] = 0.5

# ==================== Main Process ====================
for day in game_data:
    print("\nProcessing " + day + "...")
    attacks = game_data[day]["attacks"]

    # Remove people from the trust list that are no longer in the game:
    older_trust = trust.copy()  # copy to prevent issues
    removed = []
    for p in trust:
        # Compare to the set of players for the current day:
        if p not in game_data[day]["arguments"]:
            removed.append(p)
            older_trust.pop(p)
    if removed:
        print("The following people have been removed from the game: " + str(removed))
    trust = older_trust.copy()

    # Initialise attack ranking, set to 0 for each day:
    attack_ranking = {}
    for p in game_data[day]["arguments"]:
        attack_ranking[p] = 0

    # Calculate attack ranking:
    for attacked in attacks:
        attack_level = 0
        for attacker in attacks[attacked]:
            # Sum the trust values of the attackers:
            attack_level += trust[attacker]
        # Divide by the trust value of the attacked player:
        attack_ranking[attacked] = round(attack_level/trust[attacked], 2)

    # ==================== Deception ====================
    # Order the trust and attack dictionaries:
    ordered_trust = {k: v for k, v in sorted(trust.items(), key=lambda item: item[1])}.items()
    ordered_attacks = {k: v for k, v in sorted(attack_ranking.items(), key=lambda item: item[1])}.items()

    # Calculate deception:
    deception = {}
    for p in game_data[day]["arguments"]:
        dec = 0

        # Get the index in the list of trust values:
        if trust[p] >= 0.5:  # only consider players with a trust score below 0.5
            dec += np.inf
        else:
            trust_count = 0
            for (player, _) in ordered_trust:
                if p == player:
                    dec += trust_count
                else:
                    trust_count += 1

        # Get the index in the list of attack values:
        attack_count = 0
        for (player, _) in ordered_attacks:
            if p == player:
                dec += attack_count
            else:
                attack_count += 1

        # Set the deception to the sum of the index in the list of trust and attack values:
        deception[p] = dec

    # Get the player with the lowest value:
    # (someone is deceptive if they have a low trust value and a low attack value)
    min_p = min(deception, key=deception.get)
    if trust[min_p] < 0.5:  # player's trust needs to be below 0.5
        most_deceptive = min_p
    else:
        most_deceptive = "unable to be determined"

    # ==================== Output ====================
    # Print the trust values, attack levels, and the most deceptive player:
    print("Trust values:")
    print(trust)
    print("Attack levels:")
    print(attack_ranking)
    print("Most deceptive player: " + most_deceptive + "\n")

    # Ask user to perform action before going to the next iteration:
    if day is not list(game_data.keys())[-1]:
        input("Press the return key to continue to the next day\n")

    # ==================== Trust Updating ====================
    # Retrieve context information:
    rules = trust_data[day]["rules"]
    observations = trust_data[day]["observations"]

    # Check each observation:
    for a in observations:
        # Split each observation into the action and the player:
        action = a.rsplit(' ', 1)[0]
        player = a.rsplit(' ', 1)[1]

        # Access the previous trust value:
        old_trust = trust[player]

        # Compare actions with positive feedback rules:
        if action in rules["positive"]:
            new_trust = old_trust * 1.4     # multiply with positive parameter, requires tuning to use case
            if new_trust > 1:               # limit trust score at 1.0
                new_trust = 1
            trust[player] = new_trust

            # Show update process to user:
            diff = round(abs(trust[player] - old_trust), 2)
            if diff > 0:
                print(player + "'s score went up by " + str(diff) + " because they made a " + action)
            else:
                print(player + "'s score didn't change because they already have the highest possible score")

        # Compare actions with negative feedback rules:
        elif action in rules["negative"]:
            new_trust = old_trust * 0.6     # multiply with negative parameter, requires tuning to use case
            trust[player] = new_trust

            # Show update process to user:
            diff = round(abs(trust[player] - old_trust), 2)
            print(player + "'s score went down by " + str(diff) + " because they made a " + action)
