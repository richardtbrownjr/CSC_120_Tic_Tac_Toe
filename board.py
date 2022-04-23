# CSC_120_Tic_Tac_Toe
import os
import sqlite3
import traceback
import sys

board = ["-","-","-","-","-","-","-","-"]
user = True
turn = 0
#https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

def printboard(board):
    os.system('clear')
    print("Printing Board")
    #print(board)
    for i in range(0, 9, 3):
        print(*board[i:i+3], sep=' ')
        print()
    print("board printed")
    #print("Here is the turn", turn)
    whowon(board,playerup,turn)

def checkboard(userinput, board, playerup):
    if board[userinput] == "-":
        userinput = userinput-1
        board.insert(userinput, playerup)
        printboard(board)
    else:
        print("position already taken")
    try:
        sqliteConnection = sqlite3.connect('tic_tac.db')
        con = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        con.execute("DROP TABLE IF EXISTS gametable")

        sqlite_select_Query = "select sqlite_version();"
        con.execute(sqlite_select_Query)
        record = con.fetchall()
        print("SQLite Database Version is: ", record)

        con.execute("CREATE TABLE gametable(col1)")
        con.executemany("INSERT INTO gametable(col1) VALUES (?)", (board))

        con.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def whowon(board,playerup,turn):
    #print("Turn at", turn)
    #across
    if turn>3:
        if (board[0] and board[1] and board[2]) == playerup:
            print("Player", playerup, "won")
            quit()
        if (board[3] and board[4] and board[5]) == playerup:
            print("Player", playerup, "won")
            quit()
        if (board[6] and board[7] and board[8]) == playerup:
            print("Player", playerup, "won")
            quit()
        #up and down wins
        if (board[0] and board[3] and board[6]) == playerup:
            print("Player", playerup, "won")
            quit()
        if (board[1] and board[4] and board[7]) == playerup:
            print("Player", playerup, "won")
            quit()
        if (board[2] and board[5] and board[8]) == playerup:
            print("Player", playerup, "won")
            quit()
        #diagonal wins
        if (board[0] and board[4] and board[8]) == playerup:
            print("Player", playerup, "won")
            quit()
        if (board[2] and board[4] and board[6]) == playerup:
            print("Player", playerup, "won")
            quit()

def quit1(userinput):
    if userinput == 11:
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
    userinput = int(input("Please enter 1-9 or 11 to quit: "))
    turn = turn + 1
    if quit1(userinput):
        break
    if userinput in range(1,9):
        checkboard(userinput, board, playerup)
    user = not user

#https://docs.gitlab.com/ee/user/project/repository/gpg_signed_commits/#associate-your-gpg-key-with-git
os.system('clear')
printboard(board)
