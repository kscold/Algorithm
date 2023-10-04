import time
import sys

def findMinBill(money, amount, depth):
    if amount < 0:
        result = -sys.maxsize
    elif depth == len(money):
        if amount == 0:
            result = 0
        else:
            result = -sys.maxsize
    else:
        result1 = findMinBill(money, amount - money[depth], depth + 1) + 1
        result2 = findMinBill(money, amount, depth + 1)
        if result1 < 0 and result2 < 0:
            result = -sys.maxsize
        elif result1 < 0 or result2 < 0:
            result = max(result1, result2)
        else:
            result = min(result1, result2)
    return result
   
#-----------------------------------------------------------------------
# return type: int
def q3(money, N, amount):
    # your code is here
    # ----------------------------------------------
    # ----------------------------------------------
    result = findMinBill(money, amount, 0)
    if result < 0:
        result = -1
    return result


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
