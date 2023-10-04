# -----------------------------------------------------------------------
'''
Homework#3

[막대기 자르기 문제] 다음 문제를 해결하고자 한다.
문제: 길이 N cm의 막대기가 있다. 이 막대기를 1 cm, 2 cm, 3 cm로 잘라서 팔려고 한다.
1 cm, 2 cm, 3 cm 막대기의 가격이 각각 P[1], P[2], P[3]라고 할 때 가장 많이 남길
수 있는 이득은 얼마인가? 이득 함수 maxprofit()을 구하시오.
예) N = 4, P = [1, 5, 8]라면 최대 이득은 10이다. (길이 2cm로 2개 만들면 5+5 = 10)

maxprofit() 함수를 다음과 같이 정의할 때 다음 문제에 답하시오.
int maxprofit(int *P, int N);   // P: 1, 2, 3cm 짜리 막대기 가격, N: 주어진 막대기 길이

입력 file 형식
N     // 입력 막대의 갯수
P[1] P[2] P[3] N1    // 첫번 째 막대에 대한 가격과 길이
P[1] P[2] P[3] N2    // 두번 째 막대에 대한 가격과 길이
P[1] P[2] P[3] N3    // 세번 째 막대에 대한 가격과 길이
:
:

조건:
1. N의 최대값은 100이다.
2. P[1], P[2], P[3]의 최대값은 10이다.

예시)
입력: input_hw3.txt
3
5 5 5 15
6 5 9 12
5 3 3 7

출력: output_hw3.txt
75
72
35

정답은 expected_hw3.txt로 주어짐
결과는 output_hw3.txt file로 출력해야 함

Dynamic programming 기법을 이용해서 아래 코드의 maxprofit 함수를 완성하시오.
'''


# -----------------------------------------------------------------------

def compare_output(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    lines1 = f1.readlines()
    lines2 = f2.readlines()

    success = True
    i = 0
    for _ in lines2:
        if lines1[i].strip() != lines2[i].strip():
            print("[%i] Wrong answer: Yours=\'%s\', Expected=\'%s\'\n" % (i + 1, lines1[i].strip(), lines2[i].strip()))
            success = False
            break
        i = i + 1

    if success:
        print("Success!")
    f1.close()
    f2.close()


def maxprofit(P, N):
    # your code is here
    # ----------------------------------------------
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        max_profit = 0
        for j in range(1, 4):
            if i >= j:
                max_profit = max(max_profit, dp[i - j] + P[j])
            dp[i] = max_profit

    return dp[N]

    # ----------------------------------------------


# main code
input = open("input_hw3.txt", "r")  # input data
output = open("output_hw3.txt", "w")  # your answer

# your code is here
# -----------------------------------------------
nums = input.read().split()
N = int(nums[0])
i = 1
for _ in range(N):
    P = [0] * 4
    P[1] = int(nums[i])
    P[2] = int(nums[i + 1])
    P[3] = int(nums[i + 2])
    n = int(nums[i + 3])
    i = i + 4
    profit = maxprofit(P, n)
    # print(n, profit)
    output.write("{}\n".format(profit))
    ## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output_hw3.txt", "expected_hw3.txt")
