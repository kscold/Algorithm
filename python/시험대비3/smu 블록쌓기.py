# 1. 블록 쌓기
# 블록들이 n 개 주어진다. 모든 블록을 쌓아서 높게 만들려고 한다. 그런데 블록을 쌓으려면 무게만큼 들어올리는
# 비용이 든다. 모든 블록을 쌓는데 드는 최소의 비용을 구하시오. 예를 들면, 무게 1 인 블록과 무게 2 인 블록을 쌓으면
# 3 의 비용이 든다. (1+2)를 합친 무게 3 짜리의 블록과 무게 4 인 블록과 합치려면 기존의 무게 3 인 블록과 무게 4 인
# 블록을 합치는 것이므로 (1+2) + 4 즉 7 의 비용이 들게 된다. 최종적으로는 총 (1+2) + (1+2) + 4 = 10 의 비용이
# 든다.

# 예시)
# 입력
# 2 // 총 2 개의 입력
# 4 4 3 2 6 // 블록의 개수, 블록의 무게들의 리스트
# 3 1 2 3

# 2 3 4 6
# 5 9 15

# 1 2 3
# 3 6

# 출력
# 29
# 9

def min_cost_to_build_blocks(n, weights):
    # 무게들을 정렬
    weights.sort()

    total_cost = 0

    while len(weights) > 1:
        # 현재 가장 가벼운 블록 두 개를 선택
        block1 = weights.pop(0)
        block2 = weights.pop(0)

        # 현재 선택한 블록들을 합쳐서 새로운 블록 생성
        new_block = block1 + block2

        # 합쳐진 블록의 비용을 더함
        total_cost += new_block

        # 새로운 블록을 다시 리스트에 추가
        weights.append(new_block)

        # 리스트를 다시 정렬
        weights.sort()

    return total_cost


k = int(input())
n = []
for _ in range(k):
    n.append(list(map(int, input().split())))

for data in n:
    block_count = data[0]
    block_weights = data[1:]
    result = min_cost_to_build_blocks(block_count, block_weights)
    print(result)

# 2
# 4 4 3 2 6
# 3 1 2 3
