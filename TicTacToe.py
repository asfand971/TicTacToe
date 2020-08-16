#TicTacTOe
import sys

Board = {'A1':' ','A2':' ','A3':' ',
        'B1':' ','B2':' ','B3':' ',
        'C1':' ','C2':' ','C3':' '}
player1 = player2 = ''

def PrintBoard(board):
    print('*********')
    print('*'+'  '+'1'+' '+'2'+' '+'3'+'*') 
    print('*'+'A '+ board['A1']+'|'+board['A2']+'|'+board['A3']+'*')
    print('* ------*')
    print('*'+'B '+ board['B1']+'|'+board['B2']+'|'+board['B3']+'*')
    print('* ------*')
    print('*'+'C '+ board['C1']+'|'+board['C2']+'|'+board['C3']+'*')
    print('*********')


def Intro():
    global player1
    global player2
    Giveup = turncount = 0
    print('Enter player 1 Name:')
    player1 = input()
    print('Enter player 2 Name:')
    player2 = input()
    print('Match of TicTacToe Begins between ' + player1 + ' and ' + player2)
    while(Giveup == 0):
        if(turncount>=3):   #Checksboard for winner when atleast 4 tries are played
            if(Check(Board)):
                PrintBoard(Board)
                sys.exit()
        if (' ' not in Board.values()): #if empty spaces are finished on board exit
            print('Match Draw!')
            sys.exit() 
        PrintBoard(Board)
        print(player1 +"'s" + ' Turn:')
        turncount += 1
        Turn(Board,1)
        PrintBoard(Board)
        if(turncount>=3):   #Checksboard for winner when atleast 4 tries are played
            if(Check(Board)):
                sys.exit()
        if (' ' not in Board.values()): #if empty spaces are finished on board exit
            PrintBoard(Board)
            print('Match Draw!')
            sys.exit() 
        print(player2 +"'s" + ' Turn:')
        turncount +=1
        Turn(Board,2)
        if(turncount>=3):
            if(Check(Board)):   #Checksboard for winner when atleast 4 tries are played
                PrintBoard(Board)
                sys.exit()
        if (' ' not in Board.values()): #if empty spaces are finished on board exit
            PrintBoard(Board)
            print('Match Draw!')
            sys.exit() 
                

def Turn(board,player):
    run = 1
    while (run==1):
        print('Enter destination to mark on Board e.g "A1"')
        choice = input()
        if(player == 1):
            if (choice in board):
                if(board.get(choice,0) == ' '):
                    board[choice]='X'
                else:
                    print('The space is already occupied')
                    continue
            else:
                print('Choice does not exist in Board')
                continue
        else:
             if (choice in board):
                if(board.get(choice,0) == ' '):
                    board[choice]='O'
                else:
                    print('The space is already occupied')
                    continue
             else:
                print('Choice does not exist in Board')
                continue
        run=0


def Check(board):
    win = 0
    global player1
    global player2
    if (board['A1'] == 'O' and board['A2'] == 'O' and board['A3'] == 'O'):
        print(player2 +' wins!') #A row
        win = 1
    elif (board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O'):
        print(player2 +' wins!') #B row
        win = 1
    elif (board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == 'O'):
        print(player2 +' wins!') #C row
        win = 1
    elif (board['A1'] == 'O' and board['B1'] == 'O' and board['C1'] == 'O'):
        print(player2 +' wins!') #1 Column
        win = 1
    elif (board['A2'] == 'O' and board['B2'] == 'O' and board['C2'] == 'O'):
        print(player2 +' wins!') #2 Column
        win = 1
    elif (board['A3'] == 'O' and board['B3'] == 'O' and board['C3'] == 'O'):
        print(player2 +' wins!') #3 Column
        win = 1
    elif (board['A1'] == 'O' and board['B2'] == 'O' and board['C3'] == 'O'):
        print(player2 +' wins!') #A1,B2,C3 Diagnol
        win = 1
    elif (board['A3'] == 'O' and board['B2'] == 'O' and board['C1'] == 'O'):
        print(player2 +' wins!') #A3,B2,C1 Diagnol
        win = 1

    if (board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'X'):
        print(player1 +' wins!') #A row
        win = 1
    elif (board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X'):
        print(player1 +' wins!') #B row
        win = 1
    elif (board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X'):
        print(player1 +' wins!') #C row
        win = 1
    elif (board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'X'):
        print(player1 +' wins!') #1 Column
        win = 1
    elif (board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'X'):
        print(player1 +' wins!') #2 Column
        win = 1
    elif (board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'X'):
        print(player1 +' wins!') #3 Column
        win = 1
    elif (board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'X'):
        print(player1 +' wins!') #A1,B2,C3 Diagnol
        win = 1
    elif (board['A3'] == 'X' and board['B2'] == 'X' and board['C1'] == 'X'):
        print(player1 +' wins!') #A3,B2,C1 Diagnol
        win = 1
    if (win == 1):
        return True
    else:
        return False
Intro()
