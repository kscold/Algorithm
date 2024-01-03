# 상명대학교는 기말 고사 시행 때 학생들을 1 열로 자리 배치하고자 한다. 그런데 사회적 거리두기를 하기 위해 양
# 옆자리는 비워 두고자 한다. 다음과 같이 추가로 앉히고자 하는 학생의 수와 기존에 앉아 있는 자리의 배열이
# 주어졌을 때 학생들 모두 앉힐 수 있는지 여부를 반환하는 함수를 작성하시오. 1 은 학생이 이미 앉아 있는 좌석이고,
# 0 은 비어 있는 좌석이다.


# 3
# 1 5 1 0 0 0 1
# 3 5 0 0 0 0 0
# 2 5 1 0 0 0 1


# True
# True
# False


def can_seat_students(additional_students, seats):
    # 0으로 둘러싸인 자리 수를 계산하는 함수
    def count_empty_seats_between_students(seats):
        count, counts = 0, []
        for i, seat in enumerate(seats): # seats = [1 5 1 0 0 0 1]
            if seat == 1: # 만약 시트가 앉아 있는 1 이라면
                if i == 0 or seats[i - 1] == 0:  # 그게 좌석의 처음과 끝일 경우
                    counts.append(count // 2) # counts = [0]
                else:  # 좌석의 중간일 경우
                    counts.append(max(0, count // 2 - 1))
                count = 0 # 카운트 초기화
            else: # 시트가 비어있는 0인 경우
                count += 1 # 카운트 1 증가
        counts.append(count // 2)
        return counts

    # 비어있는 자리 수를 통해 앉힐 수 있는 학생 수를 계산하는 함수
    def calculate_students_from_seats(seats):
        return sum(seat for seat in seats)

    # 앉아있는 학생 사이, 앞, 뒤의 비어있는 자리 수를 계산
    empty_seats_between = count_empty_seats_between_students(seats)
    students_between = calculate_students_from_seats(empty_seats_between)

    # 총 앉힐 수 있는 학생 수가 추가로 앉히고자 하는 학생 수보다 크거나 같으면 True, 아니면 False
    return additional_students <= students_between


n = int(input())
test_cases = []

for _ in range(n):
    input_data = list(map(int, input().split()))
    test_cases.append(input_data)

for test_case in test_cases:
    person, sit = test_case[:2]
    seating_plan = test_case[2:]

    if 1 not in seating_plan: # 만약 배열에 1이 존재하지 않으면
        print(person <= (len(seating_plan) // 2 + len(seating_plan) % 2)) # 앉은 배치의 길이를 2로 나눈 몫과 2로 나눈 나머지 값을 더한 값이 person보다 크거가 같으면 예)
        # person 2 이고 (4 // 2 == 2) + (4 % 2 == 0) 이므로 True
        # person 3 이고 (4 // 3 == 1) + (4 % 3 == 1) 이므로  3 <= 2 성립 안함 
    else:
        result = can_seat_students(person, seating_plan)
        print(result)





