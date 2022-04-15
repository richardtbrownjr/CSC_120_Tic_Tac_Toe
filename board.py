# CSC_120_Tic_Tac_Toe
#stage 1

board = ["-","-","-","-","-","-","-","-","-",]
user = True
#https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

def printboard(board):
    print("Printing Board")
    for i in range(0, len(board), 3):
            print(*board[i:i+3], sep=' ')
            print()
        #for i in range(0, len(list), 5):
    #print(*list[i:i+5], sep='')
    print("board printed")

def checkboard(userinput, board, playerup):
    if board[userinput] == "-":
        board.insert(userinput, playerup)
        printboard(board)
    else:
        print("position already taken")

def quit(userinput):
    if userinput == "q":
        return True
    else:
        return False
def whoison(user):
    if user:
        return "x"
    else:
        return "o"

while True:
    playerup = whoison(user)
    userinput = int(input("Please enter 1-9 or 'q' to quit: "))
    if quit(userinput):
        break
    if userinput in range(1,9):
        checkboard(userinput, board, playerup)
    user = not user

#https://docs.gitlab.com/ee/user/project/repository/gpg_signed_commits/#associate-your-gpg-key-with-git

printboard(board)
