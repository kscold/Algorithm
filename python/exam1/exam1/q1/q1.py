import time

def q1(A, B):
    # your code is here
    # # ----------------------------------------------

    import sys

    limit_number = 10000
    sys.setrecursionlimit(limit_number)

    def mul(x, y):
        if y == 0:
            return 0
        elif y < 0:
            return -(x - mul(x, y + 1))
        else:
            return x + mul(x, y - 1)
    return mul(A, B)

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
    A = int(line[0])
    B = int(line[1])
    result = q1(A, B)
    print(result)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
