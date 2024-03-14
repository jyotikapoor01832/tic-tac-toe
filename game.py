def display_board( board):
    print('   |   |')
    print(' ' + board[7] +  ' | ' + board[8] +' | ' + board[9])
    print('   |   |')
    print('---|---|--')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] +' | ' + board[6])
    print('   |   |')
    print('---|---|--') 
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    

test_board = ['#','X','0','X','0','X','0','X','0','X']
display_board(test_board)

def player_input( ):
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker=input("Player 1: Do you want to choose X or O?").upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
    

def place_marker(board, marker, position):
    board[position] = marker
    
def check_win():
    pass
def choose_first():
    pass
def space_check():
    pass
def full_board_check():
    pass
def player_choice():
    pass
def replay():
    pass
