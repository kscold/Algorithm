# 정수 배열 nums 가 주어진다. 배열의 값은 모두 unique 하다. 즉 중복되는 값은 없다. nums 배열을 2 분할하여 그
# 합이 동일하게 만들고자 한다. 2 분할하여 각 분할들의 합의 값이 동일 해지는 경우의 수를 구하시오.
# 예시)

# 입력
# 2 // 총 2 개의 입력
# 8 1 2 3 4 5 6 7 8 // nums 의 길이, nums 의 값의 리스트
# 12 1 2 3 4 5 6 7 8 9 10 11 12

# 출력
# 7
# 62
# nums =[1, 2, 3, 4, 5, 6, 7, 8]의 경우는 다음 7 가지의 분할의 경우 각 분할의 합이 18 로 동일하다.
# [3, 7, 8] [1, 2, 4, 5, 6], [4, 6, 8] [1, 2, 3, 5, 7], [5, 6, 7] [1, 2, 3, 4, 8], [1, 2, 7, 8] [3, 4, 5, 6]
# [1, 3, 6, 8] [2, 4, 5, 7], [1, 4, 5, 8] [2, 3, 6, 7], [1, 4, 6, 7] [2, 3, 5, 8]

def count_equal_sum_partitions(nums):
    total_sum = sum(nums)

    # 전체 합이 홀수인 경우 두 부분 배열로 나눠서 합이 동일하게 만들 수 없음
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2
    count = [0] * (target_sum + 1) # [0이 18개]
    count[0] = 1 # 첫번째에는 1를 대입

    for num in nums:
        for i in range(target_sum, num - 1, -1):
            count[i] += count[i - num]

    return count[target_sum]


k = int(input())
n = []
for _ in range(k):
    n.append(list(map(int, input().split())))

for data in n:
    nums = data[1:]
    result = count_equal_sum_partitions(nums)
    print(result)



# 2
# 8 1 2 3 4 5 6 7 8
# 12 1 2 3 4 5 6 7 8 9 10 11 12