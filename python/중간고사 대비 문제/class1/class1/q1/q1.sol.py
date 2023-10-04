import time

#-----------------------------------------------------------------------
# return type: int
def q1(T):
    def q1(T):
        total = sum(T)
        dp = [[False] * (total + 1) for _ in range(len(T) + 1)]

        for i in range(len(T) + 1):
            dp[i][0] = True

        for i in range(1, len(dp)):
            for j in range(1, total + 1):
                dp[i][j] = dp[i - 1][j]
                if T[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - T[i - 1]]

        j = total // 2
        while j >= 0 and not dp[len(T)][j]:
            j = j - 1

        return total - 2 * j


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
