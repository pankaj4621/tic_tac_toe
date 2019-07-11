board={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
def tictac(board):
    print(" ")
    print("         |   |")
    print("       "+board[1] +" | " +board[2] +" | "+ board[3])
    #print("         |   |")
    print("     -------------")
    #print("         |   |")
    print("       "+board[4] +" | " +board[5] +" | "+ board[6])
    #print("         |   |")
    print("     -------------")
    #print("         |   |")
    print("       "+board[7] +" | " +board[8] +" | "+ board[9])
    print("         |   |")


def player_input():
    mark=""
    while mark != "X" or mark != "O":
        mark = str(input("player1 choose x or o: ").upper())
        if mark=="X":
            return ("X","O")
        elif mark=="O":
            return('O',"X")

player1,player2=player_input()

d={"player1":player1,"player2":player2}

def place_mark():
    flag = 0
    while flag != 1:
        # player 1 data
        var1 = 1
        while var1 == 1:
            #print("        Player 1 chance")
            q = int(input("Player 1 Enter Position: "))
            #p = input("Enter Value:    ").upper()
            if board[q] == " ":
                board[q] = player1
                flag = win_player(board,d)
                var1 = 0
            else:
                print("position",q,"already has a value, please enter again")


        if flag == 1:
            break

        # player 2 data
        var2 = 1
        while var2 == 1:
            #print("        Player 2 chance")
            r = int(input("Player 2 Enter Position: "))
            #s = input("Enter Value:    ").upper()
            if board[r] == " ":
                board[r] = player2
                flag = win_player(board,d)
                var2 = 0
            else:
                print("position", r, "already has a value, Please enter again")

        if flag == 1:
            break

def win_player(board,d):
    if board[1]==board[2]==board[3]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[1]==board[2]==board[3]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[4]==board[5]==board[6]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[4]==board[5]==board[6]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[9]==board[7]==board[8]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[9]==board[7]==board[8]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[9]==board[6]==board[3]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[9]==board[6]==board[3]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[8]==board[5]==board[2]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[8]==board[5]==board[2]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[7]==board[4]==board[1]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[7]==board[4]==board[1]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[1]==board[5]==board[9]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[1]==board[5]==board[9]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    elif board[3]==board[5]==board[7]==d["player1"]:
        print("***Congratulations!! Player 1 Won***")
        return 1
    elif board[3]==board[5]==board[7]==d["player2"]:
        print("***Congratulations!! Player 2 Won***")
        return 1
    else:
        return 0

print("plyer1 choose:  ",player1)
print("plyer2 choose:  ",player2)

place_mark()
tictac(board)