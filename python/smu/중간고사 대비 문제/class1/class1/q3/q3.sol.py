import time
import sys
#
# def findMinBill(money, amount, depth): # money 사용가능한 지폐 리스트, amount 목표금액, depth 햔재 고려중인 지폐 위치(인덱스)
#     if amount < 0: # amount가 음수이면
#         result = -sys.maxsize # reust에 음수의 최대값을 대입
#     elif depth == len(money): # 현재 고려중인 지폐 위치가 자페 리스트의 끝 인덱스와 같으면
#         if amount == 0: # 목표금액이 0과 같으면
#             result = 0 # 결과에 0을 대입
#         else: # 아니면
#             result = -sys.maxsize # 음수위 최대값을 대입
#     else: # 지폐 위치 인덱스가 양수이고 끝이 아니면
#         result1 = findMinBill(money, amount - money[depth], depth + 1) + 1 # 현재 지폐(money[depth])를 사용한 경우
#         result2 = findMinBill(money, amount, depth + 1) # 현재 지폐(money[depth])를 사용하지 않은 경우
#         if result1 < 0 and result2 < 0: # 둥
#             result = -sys.maxsize
#         elif result1 < 0 or result2 < 0: # result1과 result2가 둘다 음수이면 음수 중의 max를 함
#             result = max(result1, result2)
#         else:
#             result = min(result1, result2) # result1과 result2가 둘 다 양수이면 최소
#     return result
#
# #-----------------------------------------------------------------------
# # return type: int
# def q3(money, N, amount):
#     # your code is here
#     # ----------------------------------------------
#     # ----------------------------------------------
#     result = findMinBill(money, amount, 0)
#     if result < 0: # 음수일 때는 -1을 대입
#         result = -1
#     return result

def q3(money, N, amount): # money 지폐의 단위, N money 배열의 길이, amount 원하는 금액
    dp = [10001] * (amount + 1) # 0부터 n까지 만들기 위해 +1을 함

    dp[0] = 0 # dp[0]에는 0을 대입
    for i in range(N): # 0부터 moeny 종류 배열의 길이 만큼 반복
        for j in range(amount, money[i] - 1, -1): # for문을 원하는 금액부터 화폐의 종류까지 줄어들게 하므로 중복이 허용 안됨 첫번째 화폐단위를 사용해버림
            if dp[j - money[i]] != 10001:
                dp[j] = min(dp[j], dp[j - money[i]] + 1)

    if dp[amount] == 10001:
        return -1
    return dp[amount]



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
    amount = int(line[0])
    N = int(line[1])
    money = [0]*int(N)
    i = 0
    for i in range(N):
        money[i] = int(line[i+2])
        i = i + 1
    result = q3(money, N, amount)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------
    
# DO NOT EDIT. Checking answers
input.close()
output.close()
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
compare_output("output_data.txt", "expected_data.txt")
