import random

theBoard = {0:'0', 1:'1', 2:'2',
            3:'3', 4:'4', 5:'5',
            6:'6', 7:'7', 8:'8'}

ALL_SPOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def printBoard(board):
  print(board[0]+'|'+board[1]+'|'+board[2])
  print('-+-+-')
  print(board[3]+'|'+board[4]+'|'+board[5])
  print('-+-+-')
  print(board[6]+'|'+board[7]+'|'+board[8])

printBoard(theBoard)



def check_computer():

    if theBoard[0]=="×" and theBoard[1]=="×" and theBoard[2]=="×":
        print("You lose...")
        return False

    elif theBoard[3]=="×" and theBoard[4]=="×" and theBoard[5]=="×":
        print("You lose...")
        return False

    elif theBoard[6]=="×" and theBoard[7]=="×" and theBoard[8]=="×":
        print("You lose...")
        return False

    elif theBoard[0] == "×" and theBoard[3] == "×" and theBoard[6] == "×":
        print("You lose...")
        return False

    elif theBoard[1] == "×" and theBoard[4] == "×" and theBoard[7] == "×":
        print("You lose...")
        return False

    elif theBoard[2] == "×" and theBoard[5] == "×" and theBoard[8] == "×":
        print("You lose...")
        return False

    elif theBoard[0] == "×" and theBoard[4] == "×" and theBoard[8] == "×":
        print("You lose...")
        return False

    elif theBoard[2] == "×" and theBoard[4] == "×" and theBoard[6] == "×":
        print("You lose...")
        return False

    elif theBoard[3] == "×" and theBoard[4] == "×" and theBoard[5] == "×":
        print("You lose...")
        return False

    elif ALL_SPOTS == []:
        print("It's draw.haha")
        return False


def check_user():
    if theBoard[0] == "○" and theBoard[1] == "○" and theBoard[2] == "○":
        print("You win!")
        return False

    elif theBoard[3] == "○" and theBoard[4] == "○" and theBoard[5] == "○":
        print("You win!")
        return False

    elif theBoard[6] == "○" and theBoard[7] == "○" and theBoard[8] == "○":
        print("You win!")
        return False

    elif theBoard[0] == "○" and theBoard[3] == "○" and theBoard[6] == "○":
        print("You win!")
        return False

    elif theBoard[1] == "○" and theBoard[4] == "○" and theBoard[7] == "○":
        print("You win!")
        return False

    elif theBoard[2] == "○" and theBoard[5] == "○" and theBoard[8] == "○":
        print("You win!")
        return False

    elif theBoard[0] == "○" and theBoard[4] == "○" and theBoard[8] == "○":
        print("You win!")
        return False

    elif theBoard[2] == "○" and theBoard[4] == "○" and theBoard[6] == "○":
        print("You win!")
        return False

    elif theBoard[3] == "○" and theBoard[4] == "○" and theBoard[5] == "○":
        print("You win!")
        return False

    elif ALL_SPOTS == []:
        print("It's draw.haha")
        return False



game_is_on = True
while game_is_on:
    # Action of Computer
    print("\nIt's computer's turn.")
    ran_spot = random.choice(ALL_SPOTS)

    theBoard[ran_spot] = "×"

    for item in ALL_SPOTS:
        if item == ran_spot:
            ALL_SPOTS.remove(item)

    printBoard(theBoard)

    if check_computer() == False:
        game_is_on = False

    else:
        user_choice = int(input("\nIt is your turn.\nWhich left spot do you want to put your ○ ? Answer the number.\n"))

        theBoard[user_choice] = "○"

        for item in ALL_SPOTS:
            if item == user_choice:
                ALL_SPOTS.remove(item)

        printBoard(theBoard)

        if check_user() == False:
            game_is_on = False
