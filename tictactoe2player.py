#TicTacToe
board = {
    '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '
}


def printBoard():
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    print('Game starts now')
    turn = 'X'
    count = 0
    for i in range(100):
        print('')
        print("It is {}'s turn".format(turn))
        printBoard()
        move = input('Enter the position:')
            
        if board[move] == ' ':
            board[move] = turn
            count += 1
            
        elif board[move] != ' ':
            print("Aldready filled")
            continue
            
        if count >= 5:
            if ( board['1'] == board['2'] == board['3'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['4'] == board['5'] == board['6'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['7'] == board['8'] == board['9'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['1'] == board['4'] == board['7'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['3'] == board['6'] == board['9'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['2'] == board['5'] == board['8'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['1'] == board['5'] == board['9'] != ' '):
                print('{} won the match'.format(turn))
                break
            if ( board['3'] == board['5'] == board['7'] != ' '):
                print('{} won the match'.format(turn))
                break
        
        if count == 9:
            print("Game tie")
            break
            
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print('Do you want to restart the game?[Y/N]')
    choice = input()
    if choice == 'y' or choice == 'Y':
        for key in board:
            board[key] = ' '
        print('New Board')
        printBoard()
        game()
            

game()
printBoard()
