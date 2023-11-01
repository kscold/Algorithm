# 파이썬 ord 함수를 이용하여 유니코드 문자를 반환한다.
# 현재 나이트의 위치 입력받기, 입력예시 a1
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 유니코드가 a가 시작이므로 a를 빼고 1을 더해 인덱스값을 구함

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능하지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_colum = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_colum >= 1 and next_colum <= 8:
        result+=1

print(result)
