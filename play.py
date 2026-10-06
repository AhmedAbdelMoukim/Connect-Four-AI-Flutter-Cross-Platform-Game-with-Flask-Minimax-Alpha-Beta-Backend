from project import ConnectFourBoard
import copy
from flask import Flask, jsonify, request

app = Flask(__name__)

class play:
    def __init__(self):
        self.game = ConnectFourBoard()

    def HumanTurn(self, column):
        self.game.MakeMove(column, 1)

    def ComputerTurn(self):
        depth = 5
        best_score = float('-inf')
        best_move = None
        board = self.game

        for move in board.GetPossibleMoves():
            cloned_board = copy.deepcopy(board)
            cloned_board.MakeMove(move[1], 2)
            score = self.MinimaxAlphaBeta(depth - 1, cloned_board, float('-inf'), float('+inf'), 1)
            
            if score > best_score:
                best_score = score
                best_move = move[1]

        if best_move is not None:
            board.MakeMove(best_move, 2)
            print(f"Computer made a move at column: {best_move}")
        else:
            print("No valid move found for the computer.")
    def ComputerTurn2(self):
        depth = 5
        best_score = float('-inf')
        best_move = None
        board = self.game

        for move in board.GetPossibleMoves():
            cloned_board = copy.deepcopy(board)
            cloned_board.MakeMove(move[1], 1)
            score = self.MinimaxAlphaBeta2(depth - 1, cloned_board, float('-inf'), float('+inf'), 1)
            
            if score > best_score:
                best_score = score
                best_move = move[1]

        if best_move is not None:
            board.MakeMove(best_move, 1)
            print(f"Computer made a move at column: {best_move}")
        else:
            print("No valid move found for the computer.")

    def findBestMove(self, board, depth):
        best_value = float('-inf')
        best_move = None

        moves = board.GetPossibleMoves()

        for move in moves:
            new_board = copy.deepcopy(board)
            new_board.MakeMove(move[1], 2)
            value = self.MinimaxAlphaBeta(depth - 1, new_board, float('-inf'), float('+inf'), -1)
            
            if value > best_value:
                best_value = value
                best_move = move[1]

        return best_move

    def MinimaxAlphaBeta(self, depth, board, alpha, beta, player):
        if depth == 0:
            heuristic_value = board.heuristicEval(2)
            return heuristic_value

        if player == 1:
            v = float('-inf')
            successors = board.GetBoardSuccessors(2)
            for successor in successors:
                v = max(v, self.MinimaxAlphaBeta(depth - 1, successor, alpha, beta, -player))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v

        if player == -1:
            v = float('inf')
            successors = board.GetBoardSuccessors(1)
            for successor in successors:
                v = min(v, self.MinimaxAlphaBeta(depth - 1, successor, alpha, beta, -player))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v
        
    def MinimaxAlphaBeta2(self, depth, board, alpha, beta, player):
        if depth == 0:
            heuristic_value = board.heuristicEval2(1)
            return heuristic_value

        if player == 1:
            v = float('-inf')
            successors = board.GetBoardSuccessors(2)
            for successor in successors:
                v = max(v, self.MinimaxAlphaBeta(depth - 1, successor, alpha, beta, -player))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v

        if player == -1:
            v = float('inf')
            successors = board.GetBoardSuccessors(1)
            for successor in successors:
                v = min(v, self.MinimaxAlphaBeta(depth - 1, successor, alpha, beta, -player))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v
        
 

play_instance = play()

@app.route('/')
def home():
    return "Welcome to the Connect Four Game API"

@app.route('/make_move', methods=['POST'])

def make_move():
    data = request.get_json()
    column = data['column']
    if play_instance.game.GameNotOver():
        play_instance.HumanTurn(column)
        if play_instance.game.GameNotOver():
            play_instance.ComputerTurn()
        else :
            print("game over")
    else :  print("game over")
    print(play_instance.game.board)
    return jsonify({'message': 'Move made successfully'})

@app.route('/make_move2', methods=['POST'])
def make_move2():
    data = request.get_json()
    column = data['column']
    if play_instance.game.GameNotOver():
        play_instance.ComputerTurn2()
        if play_instance.game.GameNotOver():
            play_instance.ComputerTurn()
        else :
            print("game over")
    else :  print("game over")
    print(play_instance.game.board)
    return jsonify({'message': 'Move made successfully'})



@app.route('/get_board', methods=['GET'])
def get_board():
    board = play_instance.game.board.tolist()
    return jsonify({'board': board})

@app.route('/restart', methods=['GET'])
def restart():
    play_instance.game = ConnectFourBoard()  # Reset the board to all zeros
    return jsonify({'message': 'Board reset successfully'})

@app.route('/game_over', methods=['GET'])
def game_over():
    game_over_status = not play_instance.game.GameNotOver()
    print(f'Game Over: {game_over_status}')
    return jsonify({'game_over': game_over_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
