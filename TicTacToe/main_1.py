import random



####### Global variables for the game #######
theBoard = {0: '0', 1: '1', 2: '2',
            3: '3', 4: '4', 5: '5',
            6: '6', 7: '7', 8: '8'}

ALL_SPOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]


####### Functions for the game #######
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def modify_board(spot, all_spots, symbol):
    theBoard[spot] = symbol

    for item in all_spots:
        if item == spot:
            all_spots.remove(item)

    printBoard(theBoard)

def check_result(symbol):
    if (
            theBoard[0] == theBoard[1] == theBoard[2] == symbol or
            theBoard[3] == theBoard[4] == theBoard[5] == symbol or
            theBoard[6] == theBoard[7] == theBoard[8] == symbol or
            theBoard[0] == theBoard[3] == theBoard[6] == symbol or
            theBoard[1] == theBoard[4] == theBoard[7] == symbol or
            theBoard[2] == theBoard[5] == theBoard[8] == symbol or
            theBoard[0] == theBoard[4] == theBoard[8] == symbol or
            theBoard[2] == theBoard[4] == theBoard[6] == symbol
    ):

        if symbol == "×":
            print("You lose...")
            # return False
        else:
            print("You win!")
        return False

    elif ALL_SPOTS == []:
        print("It's draw.haha")
        return False

    else:
        pass

def restart():
    global theBoard
    global ALL_SPOTS
    continue_op = input("\nDo you want to try again?")
    if continue_op.lower() == "yes":
        theBoard = {0: '0', 1: '1', 2: '2',
                    3: '3', 4: '4', 5: '5',
                    6: '6', 7: '7', 8: '8'}
        ALL_SPOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        game_status = True
    else:
        game_status = False
    return game_status


####### Game Logic #######
game_is_on = True
while game_is_on:
    printBoard(theBoard)

    # Action of Computer
    print("\nIt's computer's turn.")
    cp_choice = random.choice(ALL_SPOTS)

    modify_board(spot=cp_choice, all_spots=ALL_SPOTS, symbol="×")

    if check_result(symbol="×") == False:
        if restart():
            continue
        else:
            game_is_on = False

    # Action of User
    else:
        user_choice = int(input("\nIt is your turn.\nWhich left spot do you want to put your ○ ? Answer the number.\n"))

        modify_board(spot=user_choice, all_spots=ALL_SPOTS, symbol="○")

        if check_result(symbol="○") == False:
            if restart():
                continue
            else:
                game_is_on = False
