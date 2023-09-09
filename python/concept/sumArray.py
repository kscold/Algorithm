ar1 = list(map(int, input().split())) # int 형식의 input을 공백을 기준으로 받아 list로 설정
print(ar1)
index = len(ar1)
print(type(index))

ar2 = list()
for i in range(0, index):
    ar2.append(sum(ar1[:i+1])) # 처음요소부터 i까지 리스트를 합하여 ar2 요소에 추가함

print(ar2)