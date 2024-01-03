import time

def q2(n):
    # your code is here
    # ----------------------------------------------

    memo = {}
    result = []
    for i in range(n):
        if i < 10:
            memo[i] = str(i)
        else:
            memo[i] = chr(55 + i)
    # N = int(input())
    while True:
        if n == 0:
            break
        x = n % 2
        result.append(memo[x])
        n //= 2
    return memo[n]
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
            print("[%i] Wrong answer: Yours=\'%s\', Expected=\'%s\'\n" % (i+1, lines1[i].strip(), lines2[i].strip()))
            success = False
            break
        i = i + 1

    if success:
        print("Success!")
    f1.close()
    f2.close()


# main code
input = open("input.txt", "r")      # input data
output = open("output.txt", "w")    # your answer

start_time = time.time()
line = input.readline().split()
K = int(line[0])
for _ in range(K):
    line = input.readline().split()
    n = int(line[0])
    result = q2(n)
    result2 = q2(result)
    if result2 != n:
        print('Error')
    print(result)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------
    
# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
