# Tic tac toe game

class Game:

    def __init__(self):
        # Board has 9 elements with 
        # 0 - Empty; 1 - X; 2 - O
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.turn = 0

    # Function to display the board
    def display_board(self):
        print('-' * 13)
        for i in range(3):
            print('|', end=' ')
            for j in range(3):
                if self.board[i][j] == 0:
                    char = str(3*i + j+1)
                elif self.board[i][j] == 1:
                    char = 'X'
                else:
                    char = 'O'
                print(char + ' | ', end='')
            print('\n' + '-' * 13)

    # Helper functions
    def get_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (3*i + j + 1)
        return -1

    # Makes the move at the given position and changes the current turn
    def make_move(self, position):
        position -= 1
        i = position//3
        j = position%3
        # If an element already exist in the position
        if self.board[i][j] != 0:
            return False
        self.board[i][j] = self.turn+1
        self.turn = ~self.turn & 1
        return True

    # Returns the winner if the game is over; -1 of game is a draw; 0 if game is not yet over
    def is_game_over(self):
        for i in range(3):
            # Horizontal check
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            
            # Vertical check
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
            
        # Diagonal Check
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[1][1]
        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return self.board[1][1]
        
        if self.get_empty() != -1:
            return 0
        return -1
    




game = Game()

# Two Player Game
while True:
    game.display_board()
    print('X' if game.turn == 0 else 'O' + "'s position :", end='')
    try:
        pos = int(input())
    except ValueError:
        exit()
    if not game.make_move(pos):
        print('Element already present in the given position. \nPlease select another position')
    status = game.is_game_over()
    if status == 1:
        print("X Wins. Congratulations!!")
    elif status == 2:
        print("Y wins. Congratulations!!")
    elif status == -1:
        print("It's a draw. Well Played")
    if status:
        game.display_board()
        break

