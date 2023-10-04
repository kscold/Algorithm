import time

#-----------------------------------------------------------------------
# return type: int
def q3(f1, f2, n):
    dp = [0]*(n+1)

    if n == 1:
        return f1
    dp[1] = f1
    if n == 2:
        return f2
    dp[2] = f2

    for i in range(3, n+1):
        dp[i] = 2*dp[i-1] + 3*dp[i-2]

    return dp[n]


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
    f1 = int(line[0])
    f2 = int(line[1])
    n = int(line[2])
    result = q3(f1, f2, n)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
compare_output("output_data.txt", "expected_data.txt")
