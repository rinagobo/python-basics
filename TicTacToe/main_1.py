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



def check_result():
    if ALL_SPOTS == []:
        print("It's draw.haha")
        return False

    elif(
            theBoard[0] == theBoard[1] == theBoard[2] == "×" or
            theBoard[3] == theBoard[4] == theBoard[5] == "×" or
            theBoard[6] == theBoard[7] == theBoard[8] == "×" or
            theBoard[0] == theBoard[3] == theBoard[6] == "×" or
            theBoard[1] == theBoard[4] == theBoard[7] == "×" or
            theBoard[2] == theBoard[5] == theBoard[8] == "×" or
            theBoard[0] == theBoard[4] == theBoard[8] == "×" or
            theBoard[2] == theBoard[4] == theBoard[6] == "×" or
            theBoard[3] == theBoard[4] == theBoard[5] == "×"
    ):
        print("You lose...")
        return False

    elif (
            theBoard[0] == theBoard[1] == theBoard[2] == "○" or
            theBoard[3] == theBoard[4] == theBoard[5] == "○" or
            theBoard[6] == theBoard[7] == theBoard[8] == "○" or
            theBoard[0] == theBoard[3] == theBoard[6] == "○" or
            theBoard[1] == theBoard[4] == theBoard[7] == "○" or
            theBoard[2] == theBoard[5] == theBoard[8] == "○" or
            theBoard[0] == theBoard[4] == theBoard[8] == "○" or
            theBoard[2] == theBoard[4] == theBoard[6] == "○" or
            theBoard[3] == theBoard[4] == theBoard[5] == "○"
    ):
        print("You win!")
        return False

    else:
        pass


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

    if check_result() == False:
        continue_op = input("\nDo you want to try again?")
        if continue_op.lower() == "yes":
            theBoard = {0: '0', 1: '1', 2: '2',
                        3: '3', 4: '4', 5: '5',
                        6: '6', 7: '7', 8: '8'}

            ALL_SPOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            continue
        else:
            game_is_on = False

    # Action of User
    else:
        user_choice = int(input("\nIt is your turn.\nWhich left spot do you want to put your ○ ? Answer the number.\n"))

        theBoard[user_choice] = "○"

        for item in ALL_SPOTS:
            if item == user_choice:
                ALL_SPOTS.remove(item)

        printBoard(theBoard)

        if check_result() == False:
            continue_op = input("\nDo you want to try again?")
            if continue_op.lower() == "yes":
                theBoard = {0: '0', 1: '1', 2: '2',
                            3: '3', 4: '4', 5: '5',
                            6: '6', 7: '7', 8: '8'}

                ALL_SPOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                continue
            else:
                game_is_on = False

   
   

