import queue


class State:
    def __init__(self, board, goal, movse=0):
        self.board = board
        self.moves = movse
        self.goal = goal

    # 스왑하는 메서드
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    # 실제 계산 메서드
    def expand(self, moves):
        result = []
        i = self.board.index(0)  # 0의 index를 찾아서 i에 대입
        if not i in [0, 1, 2]:  # 첫번째 줄에 있지 않으면
            result.append(self.get_new_board(i, i - 3, moves))

        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i - 1, moves))

        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i + 1, moves))

        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i + 3, moves))

        return result

    def f(self):
        return self.h() + self.g()

    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    def g(self):
        return self.moves

    def __lt__(self, other):  # x < y 를 판단하는 기준을 정의
        return self.f() < other.f()

    def __str__(self):
        return "---------------- f(n)=" + str(self.f()) + "\n" + \
            "---------------- h(n)=" + str(self.h()) + "\n" + \
            "---------------- g(n)=" + str(self.g()) + "\n" + \
            str(self.board[:3]) + "\n" + \
            str(self.board[3:6]) + "\n" + \
            str(self.board[6:]) + "\n" + \
            "----------------"


puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

open_queue = queue.PriorityQueue()  # 우선순위 큐 생성
open_queue.put(State(puzzle, goal))

closed_queue = []
moves = 0
while not open_queue.empty():

    current = open_queue.get()  # puzzle 리스트를 current에 담음
    print(current)

    if current.board == goal:  # goal 리스트랑 같으면
        print("탐색 성공")
        break

    moves = current.moves + 1  # 1칸 이동

    for state in current.expand(moves):
        if state not in closed_queue:
            open_queue.put(state)
        closed_queue.append(current)

    else:
        print("탐색 실패")
