import datetime
import random
from colorama import Fore


game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]

def print_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] =="X":
                print('\033[31m',game[i][j],end="\033[0m ")
            elif game[i][j] =="O":
                print('\033[34m',game[i][j],end=" \033[0m ")
            else:
                print(game[i][j],end=" ")
        print()

def player(mark,pc):
    while True:
        if pc=="Y":
            i=random.randint(0,2)
            j=random.randint(0,2)
            if game[i][j]=='-':
                game[i][j]=mark
                break
        else:
            row=int(input("enter row::"))
            col=int(input("enter col::"))
            if 0 <= row <= 2  and 0 <= col <= 2:
                if game[row][col]=='-':
                    game[row][col]=mark
                    break
                else:
                    print('that cell not empety!!!')
            else:
                print('row or col isn\'t between 0 and 2')

def row_check(row , mark):
    if game[row][0]==mark and game[row][1]==mark and game[row][2] == mark:
        print('win',mark)
        print('🎊👏👏🎊')
        return "Y"
    else:
        return "N"
        
def col_check(col, mark):
    if game[0][col]==mark and game[1][col]==mark and game[2][col] ==mark:
        print('win',mark)
        print('🎊👏👏🎊')
        return "Y"
    else:
        return "N"
        
def dia_check(row , col, mark):
    if game[row][col]==mark and game[row+1][col+1]==mark and game[row+1][col+1]==mark:
        print('win',mark)
        print('🎊👏👏🎊')
        return "Y"
        
    elif game[row][col+2]==mark and game[row+1][col+1]==mark and game[row+2][col] == mark:
        print('win',mark)
        print('🎊👏👏🎊')
        return "Y"
    else:
        return "N"
        
def Exit_game(ret,time_start):

    if ret=="Y":
        time_end=datetime.datetime.now()
        time= time_end-time_start
        print("time game::",time)
        exit()

def check_game(time):
    for i in range (3):
        a=row_check(i,"O")
        Exit_game(a,time)
        a=row_check(i,"X")
        Exit_game(a,time)
        a=col_check(i,'O')
        Exit_game(a,time)
        a=col_check(i,'X')
        Exit_game(a,time)
    a=dia_check(0,0,"O")
    Exit_game(a,time)
    a=dia_check(0,0,"X")
    Exit_game(a,time)
    
    for i in range (3):
        for j in range(3):
            if game[i][j] != "-":
                a="N"
            else:
                a="Y"
                break
        if a=="Y":
            break
    if a=="N":
        Exit_game("Y",time)
        
            

nom_player=input("1.one player or 2. two players::")

print_board()

if nom_player =="1":
    time_start=datetime.datetime.now()
    while True:
        print ("player::")
        player("X","n")
        print_board()
        check_game(time_start)
        print("pc::")
        player("O","Y")
        print_board()
        check_game(time_start)
else:
    time_start=datetime.datetime.now()
    while True:
        print ("player::")
        player("X","n")
        print_board()
        check_game(time_start)
        print("pc::")
        player("O","n")
        print_board()
        check_game(time_start)
