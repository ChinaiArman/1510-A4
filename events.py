"""
Arman Chinai | A01317650
Lex Wong | A01322278

A python module containing the event functions for Fish or Flirt.
"""


from random import randint
from time import sleep
import dialogue
import ascii_art as asc


WATER_TILE = "\U0001F30A"
LAND_TILE = "\U0001F3D6"
BOAT_TILE = "\U000026F5"
ISLAND_TILE = "\U0001F334"
PLAYER_TILE = "\U0001F3A3"
SKULL_TILE = "\U0001F480"
LEVIATHAN_TILE = "\U00002757"
FISHABLE_ITEMS = {0: "stick", 1: "stick", 2: "stick", 3: "stick", 5: "stick", 6: "boot", 7: "boot",
                  8: "boot", 9: "fishie", 10: "fishie", 11: "fishie", 12: "pufferfishie", 13: "penguin", 14: "shark",
                  15: "POSEIDON'S TRIDENT", 16: "none", 17: "none", 18: "none", 19: "none", 20: "none"}


def fishing_game(character):
    print(asc.fishing_rod)
    print(dialogue.start_fish[randint(0, len(dialogue.start_fish) - 1)])
    for i in range(randint(2, 7)):
        print("...\n\n")
        sleep(1)
    fished_item = FISHABLE_ITEMS[randint(0, 20)]
    if fished_item != "none":
        print(asc.bucket)
        if fished_item == "POSEIDON'S TRIDENT":
            for i in range(2):
                print("...\n\n")
                sleep(1)
            print(asc.fishing_ascii[fished_item])
            print("[LEX] SPECIAL DIALOGUE FOR RECEIVING TRIDENT")
        else:
            sleep(1)
            print(asc.fishing_ascii[fished_item])
            print(f"You fished a {fished_item}! It has been added to your inventory.")
        character["inventory"] += [fished_item]
        character["luck"] += 1
    else:
        print(asc.sadness)
        print("[LEX] FISH FAILURE MESSAGE")
    sleep(2)


def leviathan_event(board, character, event_dialogue):
    leviathan_charisma = 100
    leviathan_difficulty = 100
    position = (character['x-coordinate'], character['y-coordinate'])
    print(asc.leviathan)
    dialogue.slow_print(dialogue.encounter_leviathan)
    flirting = True
    while flirting:
        player_options = ["Fish and Flirt"]
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print("[LEX] MIXED FISH AND FLIRT DIALOGUE")
            if character["charisma"] > randint(0, leviathan_charisma) and character["luck"] > \
                    randint(0, leviathan_difficulty):
                print("[LEX] SUCCESS ART")
                dialogue.slow_print(dialogue.leviathan_defeated)
                character["charisma"] += 15
                character["luck"] += 15
                character["inventory"] += ["Leviathan", "An Unspoken Level of Rod-ly-ness"]
                flirting = False
            else:
                print("[LEX] FAIL ART AND DIALOGUE")
        else:
            print(event_dialogue["invalid_flirt"])
    board[position] = WATER_TILE
    board[(1, 8)] = LEVIATHAN_TILE
    character["xp"] += 1
    return


def pirate_event(board, character, event_dialogue):
    pirate_charisma = 100
    position = (character['x-coordinate'], character['y-coordinate'])
    dialogue.slow_print(event_dialogue["encounter"])
    print(event_dialogue["start_flirt"])

    flirting = True
    while flirting:
        player_options = ["Seduce"]
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(event_dialogue["seduction"][randint(0, len(event_dialogue["seduction"]) - 1)])
            if character["charisma"] > randint(0, pirate_charisma):
                print("[LEX] PIRATE BLUSH ART")
                print(event_dialogue["success"])
                character["charisma"] += 5
                character["luck"] += 5
                character["inventory"] += [event_dialogue["entity"]]
                flirting = False
            else:
                print("[LEX] PIRATE FAIL ART")
                print(event_dialogue["fail"])
        else:
            print("[LEX] CONFUSION ART")
            print(event_dialogue["flee"][randint(0, len(event_dialogue["flee"]) - 1)])

    board[position] = ISLAND_TILE
    board[(1, 8)] = LEVIATHAN_TILE
    character["xp"] += 1
    return


def boat_event(board, character, event_dialogue):
    position = (character['x-coordinate'], character['y-coordinate'])
    print(event_dialogue["ascii_encounter"])
    dialogue.slow_print(event_dialogue["encounter"])
    dialogue.slow_print(event_dialogue["acquisition"])
    board[position] = WATER_TILE
    character["xp"] += 1
    character["inventory"] += [event_dialogue["entity"]]
    return


def land_event(_, character, event_dialogue):
    entity_charisma = randint(80, 100)
    print(event_dialogue["ascii_encounter"])
    print(event_dialogue["encounter"][(randint(0, len(event_dialogue["encounter"]) - 1))])
    print(event_dialogue["start_flirt"])

    flirting = True
    while flirting:
        player_options = ("Flirt", "Flirt Harder")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(event_dialogue["flirt_dialogue"][randint(0, len(event_dialogue["flirt_dialogue"]) - 1)])
            valid_selection = True
        elif selection == "2":
            dialogue.slow_print(event_dialogue["flirt_harder_dialogue"][randint(
                0, len(event_dialogue["flirt_harder_dialogue"]) - 1)])
            valid_selection = True
        else:
            print(event_dialogue["invalid_flirt"])
            valid_selection = False

        if valid_selection:
            if character["charisma"] > randint(0, entity_charisma):
                print(event_dialogue["ascii_blushing"])
                print(event_dialogue["success_dialogue"])
                character["charisma"] += character["charisma"] < 80
                character["inventory"] += [event_dialogue["entity"]]
                flirting = False
            else:
                print(event_dialogue["ascii_fail"])
                print(event_dialogue["fail_dialogue"])
    return


def water_event(_, character, event_dialogue):
    entity_charisma = randint(80, 100)
    entity_difficulty = randint(80, 100)
    print(event_dialogue["ascii_encounter"])
    print(event_dialogue["encounter"][(randint(0, len(event_dialogue["encounter"]) - 1))])

    attempting = True
    while attempting:
        player_options = ("Fish", "Flirt")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            print(event_dialogue["fishing_rod"])
            dialogue.slow_print(event_dialogue["start_fish"][randint(0, len(event_dialogue["start_fish"]) - 1)])
            if character["luck"] > randint(0, entity_difficulty):
                print(event_dialogue["ascii_bucket"])
                print(event_dialogue["fishing_success_dialogue"])
                character["luck"] += character["luck"] < 80
                character["inventory"] += [event_dialogue["entity"]]
                attempting = False
            else:
                print(event_dialogue["ascii_fishing_fail"])
                print(event_dialogue["fishing_fail_dialogue"])
        elif selection == "2":
            print(event_dialogue["start_flirt"])
            dialogue.slow_print(event_dialogue["flirt_dialogue"][randint(0, len(event_dialogue["flirt_dialogue"]) - 1)])
            if character["charisma"] > randint(0, entity_charisma):
                print(event_dialogue["ascii_blushing"])
                print(event_dialogue["flirt_success"])
                character["charisma"] += character["charisma"] < 80
                character["inventory"] += [event_dialogue["entity"]]
                attempting = False
            else:
                print(event_dialogue["ascii_fail"])
                print(event_dialogue["flirt_fail"])
        else:
            print(event_dialogue["invalid_flirt"])
    return


def main():
    pass


if __name__ == "__main__":
    main()