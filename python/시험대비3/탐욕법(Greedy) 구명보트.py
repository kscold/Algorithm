# people = [70,50,80, 50]
# limit = 100

# 70 50 80 50
# 100

def solution(people, limit):
    answer = 0
    people.sort()  # 가벼운 순서대로 정렬 50 50 70 80
    start = 0  # 가장 가벼운 사람
    end = len(people) - 1  # 가장 무거운 사람

    while (start <= end):  # 두 명씩 구출해서 다 구출할 때까지 비교
        if (people[start] + people[end] <= limit):  # limit 보다 작거나 같으면 둘다 구출 가능
            start += 1
            end -= 1
        else:  # 안되면 일단 몸무게 큰 사람부터 먼저 구출
            end -= 1
        answer += 1
    return answer


a = list(map(int, input().split()))
b = int(input())

print(solution(a, b))

