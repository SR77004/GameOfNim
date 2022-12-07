from games import *

class GameOfNim(Game):
    def __init__(self, board):
        moves = []
        for i in range(len(board)):
            for j in range(1, board[i] + 1):
                moves.append((i, j))
        self.initial = GameState(to_move="MAX", utility=1, board=board, moves=moves)

    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()
        (index, remove) = move
        board[index] -= remove
        moves = []
        for i in range(len(board)):
            for j in range(1, board[i] + 1):
                moves.append((i, j))
        return GameState(
            to_move=("MAX" if state.to_move == "MIN" else "MIN"),
            utility=(-1 if state.to_move == "MIN" else 1),
            board=board,
            moves=moves,
        )

    def actions(self, state):
        return state.moves

    def terminal_test(self, state):
        return True if len(state.moves) == 0 or sum(state.board) == 0 else False

    def utility(self, state, player):
        return state.utility if player == "MAX" else -state.utility

    def to_move(self, state):
        return state.to_move


if __name__ == "__main__":
    nimgame = GameOfNim(board=[0, 5, 3, 1])
    print(nimgame.initial.board)
    print(
        nimgame.initial.moves
    )
    print(nimgame.result(nimgame.initial, (1, 2)))
    utility = nimgame.play_game(alpha_beta_player, query_player)
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")