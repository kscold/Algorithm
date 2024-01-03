# 보물 나누어 갖기
# k 명으로 구성된 도둑 일당이 금고를 훔쳤다. 금고 안에는 보물이 정수 배열 형태로 들어 있었다. 보물을 k 명이
# 균등하게 나누어 가질 수 있는지 계산하는 함수를 작성하시오.
# 예시)
# 입력
# 2 // 총 2 개의 입력
# 4 7 4 3 2 3 5 2 1 // 4 명의 도둑, 보물의 개수 7, 보물의 가치 4, 3, 2, 3, 5, 2, 1
# 3 4 1 2 3 4 // 3 명의 도둑, 보물의 개수 4, 보물의 가치 1, 2, 3, 4
# 출력
# True // 4 명이서 (4, 1), (3, 2), (3, 2), (5)로 나누어 가지면 된다.
# False

def can_divide_treasure(k, treasure):  # k는 도둑 수, treasure는 보물의 데이터
    total_value = sum(treasure)  # 보물의 총 가치

    # 보물의 총 가치가 k로 나누어 떨어지지 않으면 나누어 가질 수 없음
    if total_value % k != 0:
        return False

    # 나누어 가질 수 있는 보물의 가치(인당 나눠가져 가야되는 보물)
    target_value = total_value // k

    # 가치가 큰 순서대로 정렬
    sorted_treasure = sorted(treasure, reverse=True)
    print(sorted_treasure)

    # 각 도둑이 현재까지 가진 보물의 가치를 저장하는 리스트
    thief_values = [0] * k

    # 현재까지 가진 보물의 가치와 목표 가치를 비교하면서 나누어 가질 수 있는지 확인
    for current_treasure in sorted_treasure:  # [5, 4, 3, 3, 2, 2, 1]
        for i in range(k):  # 도둑의 수 만큼 반복 4 [0, 0, 0, 0]
            if thief_values[i] + current_treasure <= target_value:  # [0, 0, 0, 0] [5, 4, 3, 3, 2, 2, 1] <=  5
                thief_values[i] += current_treasure # [5, 0, 0, 0]
                break

    # 모든 도둑이 목표 가치를 가지고 있으면 True 반환
    return all(value == target_value for value in thief_values)


k = int(input())
n = []
for _ in range(k):
    n.append(list(map(int, input().split())))
print(n)

for data in n:
    thief = data[0]
    treasure = data[2:]
    result = can_divide_treasure(thief, treasure)
    print(result)

# 2
# 4 7 4 3 2 3 5 2 1
# 3 4 1 2 3 4

# 1
# 2 4 1 2 3 4