import sys

sys.setrecursionlimit(100000)


class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.goal = goal
        self.moves = moves

    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i - 3, moves))

        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i - 1, moves))

        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i + 1, moves))

        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i + 3, moves))

        return result

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    def __str__(self):
        return str(self.board[:3]) + "\n" + \
            str(self.board[3:6]) + "\n" + \
            str(self.board[6:]) + "\n" + \
            "----------------"


puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


def dfs(current, visited):
    print(current)

    if current.board == goal:
        print("탐색 성공")
        return True

    visited.add(tuple(current.board))

    for state in current.expand(current.moves + 1):
        if tuple(state.board) not in visited:
            if dfs(state, visited):
                return True


initial_state = State(puzzle, goal)
dfs(initial_state, set())
