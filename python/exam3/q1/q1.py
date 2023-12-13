# 2023-2 프로그래밍트레이닝세번째시험(2023년12월13일)
# • 문제 1 (q1) 스타트업 차리기(35점)
# • 김상명이라는 학생은 졸업 후 스타트업을 차리기로 결심했다. 같이 할 팀원을 채용해야 하는데 문제는
# 채용하는 인원을 최소화 하고 싶다는 것이다. 동시에, 필요한 skill set은 모두 갖추어야 한다. 원하는
# 모든 skill set을 갖추는 최소의 인원을 구하는 프로그램을 작성하시오.

# • 입력:
# • Skill set의 종류 (1, 2, 3, … S), 스타트업 지원자 N명의 각자의 skill set 종류 들

# • 출력:
# • 필요한 모든 skill set (1, 2, 3, … S)을 갖추는 최소의 채용 인원 수

# • 조건:
# • 필요한 skill을 두 명 이상이 보유하고 있어도 상관 없음
# • 모든 skill set을 갖출 수 없다면 -1을 출력
# • Public 입력 및 정답 (input.txt, expected.txt)이외에도 hidden 입력 및 정답으로도 채점할 예정임
# • 1 ≤ S ≤ 100, 1 ≤ N ≤ 100

# • 입출력 파일 형식 및 예시:
# 3 // 입력 케이스의 수
# SN: 3 2 // S (skill set 1, 2, 3), N (지원자 수)
# 1 2 // 1번 지원자의 skill set 1, 2
# 2 3 // 2번 지원자의 skill set 2, 3
# SN: 4 2 // S (skill set 1, 2, 3, 4), N (지원자 수)
# 1 2 3 4 // 1번 지원자의 skill set 1, 2, 3, 4
# 1 3 // 2번 지원자의 skill set 1, 3
# SN: 3 2 // S (skill set 1, 2, 3), N (지원자 수)
# 2 // 1번 지원자의 skill set 2
# 3 // 2번 지원자의 skill set 3

# 출력
# 2
# 1
# -1

import time


def q1(S, N, skills):
    # your code is here
    # ----------------------------------------------
    # N # 지원자 수
    # S # 스킬셋 종류
    # skills # 한 사람당 스킬 데이터

    # print(skills)

    count = 0

    skill_tree = []
    for i in range(1, S + 1):
        skill_tree.append(i)
        # skill_tree.sort()
        # print(skill_tree) 스킬 트리 리스트

    # 합쳐서 모든 스킬 케이스를 만들기만 하면됨

    tmp = []
    count = 0

    for n_cnt in range(N):  # 지원자 수만큼 반복
        # print(skills[n_cnt])  # 한명당 스킬 데이터
        skills[n_cnt].sort()

        for i, skill in enumerate(skills):
            if skills[i] == skill_tree:
                return 1

            print(skills[i])


            print(skills[i])

            if skill in skill_tree:
                tmp.append(s)
            print(tmp)
            if set(tmp) == skill_tree:
                # print(set(tmp))
                return n_cnt
            else:
                return -1

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
    S = int(line[1])
    N = int(line[2])
    skills = []
    for _ in range(N):
        line = input.readline().split()
        skill = []
        for s in line:
            skill.append(int(s))
        skills.append(skill)
    result = q1(S, N, skills)
    print(result)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
