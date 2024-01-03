import time


def q4(n):
    # your code is here
    # ----------------------------------------------
    dp = [10001] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        if i - 1 < 0:
            break
        else:
            dp[i] = min(dp[i - 1] + 1, dp[i])
            if i % 2 == 0:
                dp[i] = min(dp[i // 2] + 1, dp[i])
    return dp[n]
    # ----------------------------------------------


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


# main code
input = open("input.txt", "r")  # input data
output = open("output.txt", "w")  # your answer

start_time = time.time()
line = input.readline().split()
K = int(line[0])
for _ in range(K):
    line = input.readline().split()
    n = int(line[0])
    result = q4(n)
    print(result)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
