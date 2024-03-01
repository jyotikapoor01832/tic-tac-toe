def sum(a,b,c):
    return a+b+c
def reverse( ):
    def printBoard(xstate,ystate):
        zero = 'X' if xstate[0] else('O' if ystate[0] else 0)
        one = 'X' if xstate[1] else('O' if ystate[1] else 1)
        two = 'X' if xstate[2] else('O' if ystate[2] else 2)
        three = 'X' if xstate[3] else('O' if ystate[3] else 3)
        four = 'X' if xstate[4] else('O' if ystate[4] else 4)
        five = 'X' if xstate[5] else('O' if ystate[5] else 5)
        six = 'X' if xstate[6] else('O' if ystate[6] else 6)
        seven= 'X' if xstate[7] else('O' if ystate[7] else 7)
        eight = 'X' if xstate[8] else('O' if ystate[8] else 8)
        
        print(f" {zero}  | {one} | {two}")
        print(f" ---|---|---")
        print(f" {three}  | {four} | {five}")
        print(f" ---|---|---")
        print(f" {six}  | {seven} | {eight}")
    def checkWin(xstate,ystate):
        wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [3,4,6]]
        for win in wins:
            if (sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3 ):
                print("X won the match")
                return 1
            if (sum(ystate[win[0]], ystate[win[1]], ystate[win[2]]) == 3 ):
                print("O won the match")
                return 0
        return -1    
        
    xstate = [0,0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0,0]
    turn = 1     # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while (True):
        printBoard(xstate,ystate)
        if turn ==1:
            print("X's turn")
            value = int(input("Please enter a value :"))
            xstate[value] = 1
        else:
            print("O's turn")
            value = int(input("Please enter a value :"))
            ystate[value] = 1
   
        cwin = checkWin(xstate,ystate)
        if cwin != -1:
            print("Match over!")
            print("Do you want to play again ?")
            val = input("yes or no : ")
            if val=="no":
                break
            elif val=="yes":
                reverse()
            else:
                break
        turn = 1- turn

reverse()