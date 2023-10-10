import time

#-----------------------------------------------------------------------
# return type: int
# def q1(T):
#     total = sum(T) # 배열의 총합이 total
#     M = [[False] * (total + 1) for _ in range(len(T) + 1)] # 이차원 리스트로 행은 len(T)+1(리스트의 길이) 갯수만큼 열은 총합 total + 1의 갯수만큼 False로 초기화
#
#     for i in range(len(T) + 1): # 배열의 길이 + 1 만큼 반복
#         M[i][0] = True # 1열의 첫번째는 전부 True로 변경
#
#         j = 1 # j는 1로 초기화
#         while i > 0 and j <= total: # i가 0보다 크고 j가 배열의 통합보다 같거나 작으면 반복
#             M[i][j] = M[i - 1][j] # 하나 전의 행을 현재 행렬에 대입
#             if T[i - 1] <= j: # i-1의 배열의 요소가 j보다 같거나 작으면
#                 M[i][j] |= M[i - 1][j - T[i - 1]] # M[i][j] 와 M[i - 1][j - T[i - 1]]의 논리합한 값을 M[i][j]에 대입한다.
#             j = j + 1 # j에 1을 더한다.
#
#     j = total // 2 # 배열의 총합을 절반으로 나누어 j에 대입한다.
#     while j >= 0 and not M[len(T)][j]: # j가 0보다 크고, 동적 프로그래밍 테이블 M의 가장 마지막 행에서 j열이 False일 때까지 반복, 이것은 두 도둑이 보물을 균등하게 나누는 경우를 찾기 위한 단계
#         j = j - 1 # j는 j - 1를 하여 조건에 맞는 j 값을 넣음
#
#     return total - 2 * j # total은 모든 보물의 총 금액이며, j는 두 도둑이 나누어 가진 금액의 절반을 나타냄, 이를 통해 두 도둑의 차이를 계산할 수 있다.

def q1(T):
    total = sum(T)  # 모든 보물 금액의 총 합을 계산합니다.
    total //= 2  # 두 도둑이 나눠가져야 하는 금액은 총 금액의 절반입니다.

    dp = [0] * (total + 1)  # 동적 프로그래밍 배열 dp를 초기화합니다.
    dp[0] = 1  # dp[0]은 1로 초기화합니다.

    for num in T:
        for i in range(total, num - 1, -1):
            if dp[i - num]:
                dp[i] = 1

    # 최소 차이를 찾을 때, total이 홀수인 경우와 짝수인 경우를 모두 고려합니다.
    # total이 홀수인 경우, 최소 차이는 (total // 2) - i 또는 (total // 2) - (i - 1) 중 작은 값입니다.
    # total이 짝수인 경우, 최소 차이는 (total // 2) - i 입니다.
    min_diff = total
    for i in range(total // 2 + 1):
        if dp[i]:
            if total % 2 == 1:
                min_diff = min(min_diff, min((total // 2) - i, (total // 2) - (i - 1)))
            else:
                min_diff = min(min_diff, (total // 2) - i)

    return min_diff



def compare_output(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    lines1 = f1.readlines()
    lines2 = f2.readlines()

    success = True
    i = 0
    for _ in lines2:
        if lines1[i].strip() != lines2[i].strip():
            print("[%i] Wrong answer: Yours=\'%s\', Expected=\'%s\'\n" % (i+1, lines1[i].strip(), lines2[i].strip()))
            success = False
            break
        i = i + 1

    if success:
        print("Success!")
    f1.close()
    f2.close()


# main code
input = open("input_data.txt", "r")      # input data
output = open("output_data.txt", "w")    # your answer

line = input.readline().split()
K = int(line[0])
start_time = time.time()
for _ in range(K):
    line = input.readline().split()
    m = int(line[0])
    nums = [0]*int(m)
    i = 0
    for i in range(m):
        nums[i] = int(line[i+1])
        i = i + 1
    result = q1(nums)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------
    
# DO NOT EDIT. Checking answers
input.close()
output.close()
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
compare_output("output_data.txt", "expected_data.txt")
