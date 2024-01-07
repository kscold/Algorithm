# 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
# 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.


# boards = input()
# data = ["AAAA", "BB"]
# result = []
#
# i = 0
# while i < len(boards):
#     if boards[i:i + 4] == "XXXX":
#         result.append(data[0])
#         i += 4
#
#     elif boards[i:i + 2] == "XX":
#         result.append(data[1])
#         i += 2
#     elif boards[i] == "X":
#         result = ["-1"]
#         break
#     else:
#         result.append(boards[i])
#         i += 1
#
# print(''.join(result))

# replace 메서드를 이용한 간단한 구현
boards = input()

boards = boards.replace("XXXX", "AAAA")
boards = boards.replace("XX", "BB")

if "X" in boards:
    print(-1)
else:
    print(boards)
