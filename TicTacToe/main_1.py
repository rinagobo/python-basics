import random

# Tic Tac Toe Board
F_LINE = [0, 1, 2]
S_LINE = [3, 4, 5]
T_LINE = [6, 7, 8]

ALL_LINES = [F_LINE, S_LINE, T_LINE]
ALL_SPOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
ALL_SPOTS_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Show the Board
def show_board():
    print(F_LINE)
    print(S_LINE)
    print(T_LINE)

def check_computer():
    if ALL_SPOTS[0]=="❌" and ALL_SPOTS[1]=="❌" and ALL_SPOTS[2]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[3]=="❌" and ALL_SPOTS[4]=="❌" and ALL_SPOTS[5]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[6]=="❌" and ALL_SPOTS[7]=="❌" and ALL_SPOTS[8]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[0]=="❌" and ALL_SPOTS[3]=="❌" and ALL_SPOTS[6]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[1]=="❌" and ALL_SPOTS[4]=="❌" and ALL_SPOTS[7]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[2]=="❌" and ALL_SPOTS[5]=="❌" and ALL_SPOTS[8]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[0]=="❌" and ALL_SPOTS[4]=="❌" and ALL_SPOTS[8]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS[2]=="❌" and ALL_SPOTS[4]=="❌" and ALL_SPOTS[6]=="❌":
        print("You lose...")
        return False

    elif ALL_SPOTS_LIST == []:
        print("It's draw.haha")
        return False

def check_user():
    if ALL_SPOTS[0]=="⭕" and ALL_SPOTS[1]=="⭕" and ALL_SPOTS[2]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[3]=="⭕" and ALL_SPOTS[4]=="⭕" and ALL_SPOTS[5]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[6]=="⭕" and ALL_SPOTS[7]=="⭕" and ALL_SPOTS[8]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[0]=="⭕" and ALL_SPOTS[3]=="⭕" and ALL_SPOTS[6]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[1]=="⭕" and ALL_SPOTS[4]=="⭕" and ALL_SPOTS[7]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[2]=="⭕" and ALL_SPOTS[5]=="⭕" and ALL_SPOTS[8]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[0]=="⭕" and ALL_SPOTS[4]=="⭕" and ALL_SPOTS[8]=="⭕":
        print("You win!!!")
        return False

    elif ALL_SPOTS[2]=="⭕" and ALL_SPOTS[4]=="⭕" and ALL_SPOTS[6]=="⭕":
        print("You win!!!")
        return False

game_is_on = True
while game_is_on:
    # print(ALL_SPOTS_LIST)
    # print(ALL_SPOTS)

    # Action of Computer
    print("\nIt's computer's turn.")
    ran_spot = random.choice(ALL_SPOTS_LIST)

    for spot in F_LINE:
        if spot == ran_spot:
            spot_index = F_LINE.index(spot)
            F_LINE = F_LINE[:spot_index]+["❌"]+F_LINE[spot_index+1:]
            # print(F_LINE)

    for spot in S_LINE:
        if spot == ran_spot:
            spot_index = S_LINE.index(spot)
            S_LINE = S_LINE[:spot_index] + ["❌"] + S_LINE[spot_index + 1:]
            # print(S_LINE)

    for spot in T_LINE:
        if spot == ran_spot:
            spot_index = T_LINE.index(spot)
            T_LINE = T_LINE[:spot_index] + ["❌"] + T_LINE[spot_index + 1:]
            # print(T_LINE)

    for spot in ALL_SPOTS:
        if spot == ran_spot:
            spot_index = ALL_SPOTS.index(spot)
            ALL_SPOTS = ALL_SPOTS[:spot_index] + ["❌"] + ALL_SPOTS[spot_index + 1:]

    for item in ALL_SPOTS_LIST:
        if item == ran_spot:
            ALL_SPOTS_LIST.remove(item)

    show_board()
    if check_computer() == False:
        game_is_on = False

    else:
        user_choice = int(input("\nIt is your turn.\nWhich left spot do you want to put your ⭕ ? Answer the number.\n"))

        for spot in F_LINE:
            if spot == user_choice:
                spot_index = F_LINE.index(spot)
                F_LINE = F_LINE[:spot_index]+["⭕"]+F_LINE[spot_index+1:]
                # print(F_LINE)

        for spot in S_LINE:
            if spot == user_choice:
                spot_index = S_LINE.index(spot)
                S_LINE = S_LINE[:spot_index] + ["⭕"] + S_LINE[spot_index + 1:]
                # print(S_LINE)

        for spot in T_LINE:
            if spot == user_choice:
                spot_index = T_LINE.index(spot)
                T_LINE = T_LINE[:spot_index] + ["⭕"] + T_LINE[spot_index + 1:]
                # print(T_LINE)

        for spot in ALL_SPOTS:
            if spot == user_choice:
                spot_index = ALL_SPOTS.index(spot)
                ALL_SPOTS = ALL_SPOTS[:spot_index] + ["⭕"] + ALL_SPOTS[spot_index + 1:]

        for item in ALL_SPOTS_LIST:
            if item == user_choice:
                ALL_SPOTS_LIST.remove(item)

        show_board()
        if check_user() == False:
            game_is_on = False
