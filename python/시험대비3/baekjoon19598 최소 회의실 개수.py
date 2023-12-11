import sys, heapq
input = sys.stdin.readline

N = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(N)]) # 튜플 형태도 제대로 sorted 하기 위해 사용 우선순위를 유지하기 위해 이차원 리스트의 첫번째 원소 기준으로 정렬
h = []

for start, end in schedules:
    if h and h[0] <= start: # 힙 리스트가 존재하고 첫번째 힙 원소(큐 이므로 왼쪽부터 들어감)가 start 보다 작을 때, 즉 회의시간이 끝나는 시간보다 시작하는 시간이 크면
        heapq.heappop(h) # 회의실을 하나 줄임
    heapq.heappush(h, end) # 끝나는시간이 시작하는 시간보다 크면 회의실을 늘림

print(len(h))