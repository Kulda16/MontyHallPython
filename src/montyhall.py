import random


def get_non_prize_door(host: int, num_doors: int, player_choice: int):
    i = 1
    while i == host or i == player_choice:
        i = (i + 1) % num_doors

    return i


def switch_function(shown_door: int, num_doors: int, player_choice: int):
    i = 1
    while i == shown_door or i == player_choice:
        i = (i + 1) % num_doors

    return i


def monty_hall_game(switch: bool, num_tests: int, show_logs: bool):
    win_switch_cnt = 0
    win_no_switch_cnt = 0
    lose_switch_cnt = 0
    lose_no_switch_cnt = 0

    doors = [0, 1, 2]
    num_doors = len(doors)

    for i in range(0, num_tests):
        door_with_prize = random.randint(0, num_doors - 1)
        host = door_with_prize
        player_choice = random.randint(0, num_doors - 1)
        original_player_choice = player_choice
        shown_door = get_non_prize_door(host, num_doors, player_choice)

        # if the player chooses to always switch, then allow the player to switch his original chosen door
        if switch:
            player_choice = switch_function(shown_door, num_doors, player_choice)

        if show_logs:
            if player_choice == door_with_prize and not switch:
                print(f"Player wins (no switch)!\n"
                      f"Original door choice: {original_player_choice}.\n"
                      f"Shown door: {shown_door}.\n"
                      f"Door with prize: {door_with_prize}.\n"
                      f"The player chose door: {player_choice}.\n"
                      f"-------------------------------------------------")
                win_no_switch_cnt += 1
            elif player_choice == door_with_prize and switch:
                print(f"Player wins (switch)!\n"
                      f"Original door choice: {original_player_choice}.\n"
                      f"Shown door: {shown_door}.\n"
                      f"Door with prize: {door_with_prize}.\n"
                      f"The player chose door: {player_choice}.\n"
                      f"-------------------------------------------------")
                win_switch_cnt += 1
            elif player_choice != door_with_prize and not switch:
                print(f"Player lost (no switch)!\n"
                      f"Original door choice: {original_player_choice}.\n"
                      f"Shown door: {shown_door}.\n"
                      f"Door with prize: {door_with_prize}.\n"
                      f"The player chose door: {player_choice}.\n"
                      f"-------------------------------------------------")
                lose_no_switch_cnt += 1
            elif player_choice != door_with_prize and switch:
                print(f"Player lost (switch)!\n"
                      f"Original door choice: {original_player_choice}.\n"
                      f"Shown door: {shown_door}.\n"
                      f"Door with prize: {door_with_prize}.\n"
                      f"The player chose door: {player_choice}.\n"
                      f"-------------------------------------------------")
                lose_switch_cnt += 1
            else:
                print('Something is wrong...')
        else:
            if player_choice == door_with_prize and not switch:
                win_no_switch_cnt += 1
            elif player_choice == door_with_prize and switch:
                win_switch_cnt += 1
            elif player_choice != door_with_prize and not switch:
                lose_no_switch_cnt += 1
            elif player_choice != door_with_prize and switch:
                lose_switch_cnt += 1
            else:
                print('Something is wrong...')

    return win_no_switch_cnt, win_switch_cnt, lose_no_switch_cnt, lose_switch_cnt, num_tests


def game_statistics(x):
    print(f"Win switch %: {x[1] / x[4]}")
    print(f"Lose switch %: {x[3] / x[4]}")
    print(f"Win no switch %: {x[0] / x[4]}")
    print(f"Lose no switch %: {x[2] / x[4]}")
    print(f"Total number of simulations: {x[4]}")
