'''We will make the board using dictioary in which keys will be the location(i.e top-left, mid-right etc.)
and intially it's value will be empty space and then after every mov.
we will change the value according to the player's choice of move.'''
theBoard={'7': ' ', '8': ' ', '9': ' ',
           '4': ' ', '5': ' ', '6': ' ',
           '1': ' ', '2': ' ', '3': ' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)
'''We will have to print the updates board after every move in the game and 
thus we will make a function in which we'll define the print Board function
so that we can easily print the board every time by calling this function.'''
def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
def game():
    turn='X'
    count=0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn,"+turn+". Move to which place?")
        move=input()
        if theBoard[move]==' ':
            theBoard[move]=turn
            count+=1
        else:
            print("The place is already occupied! \n Move to which place?")
            continue
        
        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['1']==theBoard['4']==theBoard['7']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['2']==theBoard['5']==theBoard['8']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['3']==theBoard['6']==theBoard['9']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
            elif theBoard['1']==theBoard['5']==theBoard['9']!= ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("****"+turn+"**** has won.")
                break
                
        if count==9:
            print("\nGame Over.\n")
            print("It's a Tie!")
        

        if turn=='X':
            turn='O'
        else:
            turn='X'


    restart=input("Do you want to play again? (yes/no): ")
    if restart=='yes' or restart=='y' or restart=='Yes' or restart=='Y':
        for key in board_keys:
            theBoard[key]=' '
        
        game()

if __name__=="__main__":
    game()
    