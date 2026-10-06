import numpy as np 
import copy
class ConnectFourBoard : 
    
    def __init__(self ):
        self.rows = 6
        self.cols = 7
        board = np.zeros((6, 7))
        self.board = board
    def GetPossibleMoves(self): 
        emptyPositions = []
        for col in range(self.board.shape[1]):
            column = self.board[:, col] 
            zero_indices = np.where(column == 0)[0] 
            if len(zero_indices) > 0: 
                colEmptyPosition = zero_indices[-1] 
                emptyPositions.append((colEmptyPosition, col)) 
        return emptyPositions

    def GetBoardSuccessors(self, piece):
        successors = []
        moves = self.GetPossibleMoves()

        for r, c in moves:
           
            new_board = ConnectFourBoard()
            new_board.board = self.board.copy() 

           
            new_board.MakeMove(c, piece) 

            successors.append(new_board)

        return successors
            
            
    def MakeMove(self, col, piece):
        moves = self.GetPossibleMoves()
        for move in moves:
            row = move[0]
            if move[1] == col:
                self.board[row][col] = piece
                break 
        
        
    def CheckThis(self, piece, r, c):
        if c + 3 < self.board.shape[1] and all(self.board[r][c+i] == piece for i in range(4)):
            return True
        
        if r + 3 < self.board.shape[0] and all(self.board[r+i][c] == piece for i in range(4)):
            return True
        
        if r + 3 < self.board.shape[0] and c + 3 < self.board.shape[1] and \
                all(self.board[r+i][c+i] == piece for i in range(4)):
            return True
        
        if r + 3 < self.board.shape[0] and c - 3 >= 0 and \
                all(self.board[r+i][c-i] == piece for i in range(4)):
            return True
        
        return False
    def GameNotOver (self):
        if self.win(1):
            print('Player 1 Wins!')
            return False
        elif self.win(2):
            print('Player 2 Wins!')
            return False
        elif len(self.GetPossibleMoves()) == 0:
            print('It\'s a Draw!')
            return False
        else:
            return True
    def win(self, piece):
        for r in range(self.board.shape[0]):
            for c in range(self.board.shape[1]):
                if self.board[r][c] == piece:
                    if self.CheckThis(piece, r, c):
                        return True 
        return False 

                   
    # def evaluateWinningSequences(self, piece):
       
    #     count = 0

       
    #     for row in range(self.rows):
    #         for col in range(self.cols - 3):
    #             if self.board[row][col] == piece and \
    #                     self.board[row][col + 1] == piece and \
    #                     self.board[row][col + 2] == piece and \
    #                     self.board[row][col + 3] == 0:
    #                 count += 1

       
    #     for col in range(self.cols):
    #         for row in range(self.rows - 3):
    #             if self.board[row][col] == piece and \
    #                     self.board[row + 1][col] == piece and \
    #                     self.board[row + 2][col] == piece and \
    #                     self.board[row + 3][col] == 0:
    #                 count += 1

       
    #     for row in range(self.rows - 3):
    #         for col in range(self.cols - 3):
    #             if self.board[row][col] == piece and \
    #                     self.board[row + 1][col + 1] == piece and \
    #                     self.board[row + 2][col + 2] == piece and \
    #                     self.board[row + 3][col + 3] == 0:
    #                 count += 1

       
    #     for row in range(3, self.rows):
    #         for col in range(self.cols - 3):
    #             if self.board[row][col] == piece and \
    #                     self.board[row - 1][col + 1] == piece and \
    #                     self.board[row - 2][col + 2] == piece and \
    #                     self.board[row - 3][col + 3] == 0:
    #                 count += 1

    #     return count
    # def pieceCount(self, piece):
    #     count = sum(np.count_nonzero(row == piece) for row in self.board)
    #     return count
    # def centerControl(self, piece):
       
    #     center_pieces = [list(self.board[row, 2:4]) for row in range(self.rows)]
    #     count = sum(row.count(piece) for row in center_pieces)
    #     return count
    


    def heuristicEval(self, piece):
        score = 0

       
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row][col + i] for i in range(4)]
                score += self.evaluateWindow(window, piece)

       
        for col in range(self.cols):
            for row in range(self.rows - 3):
                window = [self.board[row + i][col] for i in range(4)]
                score += self.evaluateWindow(window, piece)

       
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                score += self.evaluateWindow(window, piece)

       
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                score += self.evaluateWindow(window, piece)

        return score

    def evaluateWindow(self, window, piece):
        score = 0
        opponent_piece = 1 if piece == 2 else 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score
      
        
def heuristicEval2(self, piece):
    score = 0

    # Check horizontally
    for row in range(self.rows):
        for col in range(self.cols - 3):
            window = [self.board[row][col + i] for i in range(4)]
            score += self.evaluateWindow3(window, piece)

    # Check vertically
    for col in range(self.cols):
        for row in range(self.rows - 3):
            window = [self.board[row + i][col] for i in range(4)]
            score += self.evaluateWindow3(window, piece)

    # Check positively sloped diagonals
    for row in range(self.rows - 3):
        for col in range(self.cols - 3):
            window = [self.board[row + i][col + i] for i in range(4)]
            score += self.evaluateWindow3(window, piece)

    # Check negatively sloped diagonals
    for row in range(3, self.rows):
        for col in range(self.cols - 3):
            window = [self.board[row - i][col + i] for i in range(4)]
            score += self.evaluateWindow3(window, piece)

    return score

def evaluateWindow2(self, window, piece):
    score = 0

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    return score
