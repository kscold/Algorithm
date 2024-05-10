import sys

input = sys.stdin.readline

t = int(input())

result_list = []
for i in range(t):
    a, b = map(int, input().split())
    result_list.append(a + b)

for result in result_list:
    print(result)