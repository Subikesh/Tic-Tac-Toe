# Tic tac toe game
import math
import copy

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
    # gets the board and a n value. Returns the nth empty value from the board
    def get_empty(self, board, n=0):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    if n == 0:
                        return (3*i + j + 1)
                    n -= 1
        return -1

    # Returns the number of empty spaces in the grid
    def count_empty(self, board):
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    count += 1
        return count

    # Makes the move at the given position and changes the current turn
    def make_move(self, board, position, turn):
        position -= 1
        i = position//3
        j = position%3
        # If an element already exist in the position
        if board[i][j] != 0:
            return -1
        board[i][j] = turn+1
        turn = ~turn & 1
        return turn

    # Returns the winner if the game is over; -1 of game is a draw; 0 if game is not yet over
    def is_game_over(self, board):
        for i in range(3):
            # Horizontal check
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return board[i][0]
            
            # Vertical check
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return board[0][i]
            
        # Diagonal Check
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[1][1]
        if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return board[1][1]
        
        if self.get_empty(board) != -1:
            return 0
        return -1

    # Mini-Max Algorithm Implementation using alpha-beta pruning
    # returns the best position for the AI to make it's move
    def get_next_move(self, depth, board, turn = 1, alpha = -math.inf, beta = math.inf, maximize=True):
        winner = self.is_game_over(board)
        # Here we add it with depth, to give more preference to win it in smaller depth
        if winner:
            if winner == self.turn+1:
                return 10 - depth
            elif winner == (~self.turn & 1)+1:
                return -10 + depth
            elif winner == -1:
                return 0

        if maximize:
            max_eval = -math.inf
            for i in range(self.count_empty(board)):
                temp_board = copy.deepcopy(board)
                index = self.get_empty(temp_board, i)
                self.make_move(temp_board, index, turn)
                evall = self.get_next_move(depth+1, temp_board, ~turn&1, alpha, beta, False)
                if max_eval < evall:
                    bestpos = index
                    max_eval = evall
                alpha = max(alpha, evall)
                if beta <= alpha:
                    break
            if depth==0:
                return bestpos
            return max_eval
        else:
            min_eval = math.inf
            for i in range(self.count_empty(board)):
                temp_board = copy.deepcopy(board)
                index = self.get_empty(temp_board, i)
                self.make_move(temp_board, index, turn)
                evall = self.get_next_move(depth+1, temp_board, ~turn&1, alpha, beta, True)
                if min_eval > evall:
                    min_eval = evall
                    bestpos = index
                beta = min(beta, evall)
                if beta <= alpha:
                    break
            if depth==0:
                return bestpos
            return min_eval



def game_check(game):
    status = game.is_game_over(game.board)
    if status == 1:
        print("X Wins. Congratulations!!")
    elif status == 2:
        print("Y wins. Congratulations!!")
    elif status == -1:
        print("It's a draw. Well Played")
    if status:
        game.display_board()
        return False
    else:
        return True


game = Game()

# Two Player Game
# while True:
#     game.display_board()
#     print(('X' if game.turn == 0 else 'O') + "'s position :", end='')
#     try:
#         pos = int(input())
#     except ValueError:
#         break
#     if not game.make_move(game.board, pos, game.turn):
#         print('Element already present in the given position. \nPlease select another position')
#     status = game.is_game_over()
#     if status == 1:
#         print("X Wins. Congratulations!!")
#     elif status == 2:
#         print("Y wins. Congratulations!!")
#     elif status == -1:
#         print("It's a draw. Well Played")
#     if status:
#         game.display_board()
#         break

# Single Player game
while True:
    game.display_board()
    print(('X' if game.turn == 0 else 'O') + "'s position :", end='')
    try:
        pos = int(input())
    except ValueError:
        break
    temp = game.make_move(game.board, pos, game.turn)
    if temp == -1:
        print('Element already present in the given position. \nPlease select another position')
        continue
    game.turn = temp
    # Check before AI makes its move
    if game_check(game):
        game.turn = game.make_move(game.board, game.get_next_move(0, game.board, turn=game.turn), game.turn)
    else:
        break
    # Check after AI makes its move
    if not game_check(game):
        break
