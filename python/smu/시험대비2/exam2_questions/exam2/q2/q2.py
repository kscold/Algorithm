import time
import sys


def q2(coins, target):
    # your code is here
    # ----------------------------------------------
    def dfs(coins, target, idx):
        if target == 0:
            return 1
        answer = 0
        for i in range(idx, len(coins)):
            if coins[i] <= target:
                answer += dfs(coins, target - coins[i], i)
        return answer

    answer = dfs(coins, target, 0)
    return answer


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
    line = input.readline().strip().split(' ')
    n = int(line[0])
    coins = []
    for j in range(n):
        coins.append(int(line[j + 1]))
    target = int(line[-1])
    result = q2(coins, target)
    print(result)
    sys.stdout.flush()
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
