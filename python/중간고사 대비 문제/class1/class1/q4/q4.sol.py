import time
import sys

def bfs(graph, root, f, visited):
    depth = 1
    min_depth = sys.maxsize
    queue = []
    queue.append(root)
    while len(queue) != 0:
        size = len(queue)
        for _ in range(size):
            u = queue.pop(0)
            for v in graph[u]:
                if visited[v]:
                    continue
                visited[v] = True
                if v == f and depth < min_depth:
                    min_depth = depth
                queue.append(v)
        depth = depth + 1
    return min_depth

#-----------------------------------------------------------------------
# return type: int
def q4(friendList, friend):
    graph = [[]] * 10001
    depth = 0
    min_depth = 200

    for e in friendList:
        graph[e[0]] = graph[e[0]] + [e[1]]
        graph[e[1]] = graph[e[1]] + [e[0]]
  
    visited = [False] * 10001
    result = bfs(graph, 0, friend, visited)
    if result == sys.maxsize:
        result = -1
    return result
    # your code is here
    # ----------------------------------------------
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
input = open("input_data.txt", "r")      # input data
output = open("output_data.txt", "w")    # your answer

line = input.readline().split()
K = int(line[0])
start_time = time.time()
for _ in range(K):
    line = input.readline().split()
    m = int(line[0])
    f = int(line[1])
    edges = []
    for _ in range(m):
        line = input.readline().split()
        u = int(line[0])
        v = int(line[1])
        edges.append([u, v])
    result = q4(edges, f)
    output.write('{}\n'.format(result))
    input.readline()

end_time = time.time()
## -----------------------------------------------
    
# DO NOT EDIT. Checking answers
input.close()
output.close()
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
compare_output("output_data.txt", "expected_data.txt")
