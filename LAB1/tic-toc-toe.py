from typing import Any
import copy
import math
import collections

EMPTY = None
X = "X"
O = "O"

def createTable ():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def empty(Table):
    if Table==[[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]:
        return True
    else:
        return False


def playeris(Table):
    countx = 0
    county = 0
    for i in range(3):
        for j in range(3):
            if (Table[i][j] == X):
                countx += 1
            elif (Table[i][j] == O):
                county += 1
    if countx <= county:
        return X
    else:
        return O


def actions(Table):
    l = []
    for i in range(len(Table)):
        for j in range(len(Table)):
            if Table[i][j] == EMPTY:
                l.append((i, j))
    return(l)


def result(Table, action):
    newTable = copy.deepcopy(Table)
    i=action[0]
    j=action[1]
    if newTable[i][j]==X or newTable[i][j]==O:
        while True:
            print("This box is already filled..!!  :(")
            print("Enter valid row and column : ")
            i = int(input("Enter row : "))
            j = int(input("Enter column : "))
            i -= 1
            j -= 1
            if newTable[i][j]!=X or newTable[i][j]!=O:
                newTable[i][j] = playeris(newTable)
                return newTable
    else:
        newTable[i][j] = playeris(newTable)
        return newTable


def row_win(Table, player):
    for x in range(len(Table)):
        win = True

        for y in range(len(Table)):
            if Table[x][y] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)



def col_win(Table, player):
    for x in range(len(Table)):
        win = True

        for y in range(len(Table)):
            if Table[y][x] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


def diag_win(Table, player):
    wi = True
    y = 0
    for x in range(len(Table)):
        if Table[x][x] != player:
            wi = False
    win = True
    for x in range(len(Table)):
        y = len(Table) - 1 - x
        if Table[x][y] != player:
            win = False
    return win or wi

def winneris(Table):
    winner = EMPTY
    for player in [X, O]:
        if (row_win(Table, player) or col_win(Table, player) or diag_win(Table, player)):
            winner = player
            break
    return winner


def utility(Table):
    if winneris(Table)==X:
        return 1
    elif winneris(Table)==O:
        return -1
    else:
        return 0


def minimax(Table):
    global opt_action
    if(terminal(Table)):
        return EMPTY
    def max_value(Table):
        if terminal(Table):
            return utility(Table)
        v_max = -math.inf
        for action in actions(Table):
            v_max = max(v_max, min_value(result(Table, action)))
        return v_max

    def min_value(Table):
        if terminal(Table):
            return utility(Table)
        v_min = math.inf
        for action in actions(Table):
            v_min = min(v_min, max_value(result(Table, action)))
        return v_min

    if playeris(Table) == X:
            v = -math.inf
            for action in actions(Table):
                t = min_value(result(Table, action))
                if t > v:
                    v = t
                    opt_action = action
    else:
        v = math.inf
        for action in actions(Table):
            t = max_value(result(Table, action))
            if t < v:
                v = t
                opt_action = action
    return opt_action


def terminal(Table):
    if winneris(Table)==X or winneris(Table)==O:
        return True
    else:
        for i in range(len(Table)):
            for j in range(len(Table)):
                if Table[i][j] == EMPTY:
                    return False
        return True


def display (Table):
    print()
    for r in Table:
        for c in r:
            if c == EMPTY:
                print(" ",end = " | ")
            else:
                print(c,end = " | ")
        print()
    print()


def start ():
    user = None
    Table = createTable()
    ai_turn = False
    option = 'Y'
    while(option=='Y' or option=='y'):
        if user is None:
            user = input("Play as 'O' or 'X' : ")
            if user != X and user != O:
                print ("Enter a valid choice:")
                user = None
            else:
                print("Playing as ",user)
            continue
        else:
            game_over = terminal(Table)
            player = playeris(Table)
            if game_over:
                winner = winneris(Table)
                if winner is None:
                    print("Game Over: Tie.")
                else:
                    print("Game Over: %s wins" % winner)
                Table = createTable()
                user = None
                option = input("Press 'Y' to play again : ")
                continue
            elif user == player:
                print("Choose the row and column(both within 1 to 3) to enter %s :"% user)
                i = int(input("Enter row : "))
                j = int(input("Enter column : "))
                Table = result(Table, (i-1, j-1))
                display(Table)
            elif user != player and not game_over:
                if ai_turn:
                    print("Computer's thinking...")
                    move = minimax(Table)
                    Table = result(Table, move)
                    display(Table)
                    ai_turn = False
                    continue
                else:
                    ai_turn = True        


start()
print("Thank You :)")
