# 대표적인 O(NlogN) 알고리즘

def merge_sort(arr):
    if len(arr) < 2:  # 만약 배열 요소가 2개 이상 없다면, 즉 하나가 될때까지 처음에 쪼갬 O(logn)
        return arr

    mid = len(arr) // 2  # int(len(arr)/2) 와 같음 즉 정수로 반환 mid(반)을 정함
    low_arr = merge_sort(arr[:mid])  # 반반 리스트 슬라이싱을 이용해 재귀 호출을 이용
    high_arr = merge_sort(arr[mid:])

    merged_arr = []  # 병합할 리스트를 생성
    l = h = 0  # 0으로 초기화
    while l < len(low_arr) and h < len(high_arr):  # l h 둘다 만족해야 break
        if low_arr[l] < high_arr[h]:  # 배열의 왼쪽 요소 < 오른쪽 요소를 비교
            merged_arr.append(low_arr[l])  # 배열의 왼쪽 요소를 추가
            l += 1  # 왼쪽 요소 카운트 증가
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


A = list(map(int, input().split()))
print(merge_sort(A))


# 최적화된 코드
def merge_sort2(arr):
    def sort(low, high):  # 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용하여 입력 배열을 업데이트하여 메모리 사용량을 줄임
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:  # low < mid 이고  mid < high 배열을 병합하는 부분
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid: # 배열의 남아있는 요소들을 병합 결과에 추가
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


B = list(map(int, input().split()))
merge_sort2(B)  # B 배열을 직접 정렬
print(B)  # 정렬된 B 배열을 출력
