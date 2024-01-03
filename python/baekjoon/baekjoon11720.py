# n = input() # 갯수 하나를 임포트 받음
# # numbers = list(input()) # 인풋으로 받은 값들을 리스트로 선언한다는 뜻 그러나 이런식으로 만들면 1, 0 ,9 이런식으로 저장되기때문에 옳지 않음
# # 공백없이 사실 2자리가 되면 55가 되어야하므로 문제가 좀 틀린 문제임
# numbers = input()
# sum = 0
#
# for i in numbers:
#     sum = sum + int(i)
#
# print(sum)

n = input()
numbers = map(int, list(input()))
sum = 0

for i in numbers:
    sum = sum + i

print(sum)
