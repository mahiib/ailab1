import random as rand

from numpy import char
theBoard={
    '1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '
}

def printBoard(theBoard):
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
def randpos():
    for i in range(1000):
        x=rand.randint(1,9)
        x=str(x)
        if theBoard[x]==' ':
            break
        else:
            continue
    return x
def game():
    count =0
    chance='x'
    for i in range(10):
        printBoard(theBoard)
        if chance=='x':
            print("Enter your position "+chance)
            move=input()

            if theBoard[move]==' ':
                theBoard[move]=chance
            else:
                print("Re-enter it is taken")
                i-=1
                continue
        if chance=='o':
            theBoard[move]=chance
            
        count+=1
        if count >=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +chance + " won. ****")
                break 

        if count == 9:
            print("Draw")
        if chance=='x':
             move=randpos()
             chance='o'
        else:
            chance='x'
        
        
            

    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in range(9):
            theBoard[key+1] = " "

        game()

if __name__ == "__main__":
    game()
       




        