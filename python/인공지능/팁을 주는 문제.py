# 공부와 복습을 많이 함에 따라 학점이 잘나온다
study1 = [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.2, 0.1, 0.05] # 처음 공부 정도
review1 = [1, 1.0, 0.9, 0.9, 0.6, 0.3, 0.1, 0.1, 0.1, 0.01] # 복습 정도
grade1 = [0.0, 0.9, 0.6, 0.3, 0.7, 0.9, 0.8, 0.5, 0.2, 0.4]  # 학점에 대한 평가(A+ A B+ B C+ C D+ D F)
Result1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result1[i] = min(max(study1[8], review1[6]), grade1[i])

print(Result1)

study2 = [0, 0.2, 0.3, 0.4, 0.5, 1.0, 0.5, 0.4, 0.3, 0.1]
review2 = [0.0, 0.0, 0.2, 0.3, 0.6, 1.0, 0.6, 0.3, 0.2, 0.0]
Result2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result2[i] = min(study2[1], review2[i])

print(Result2)

study3 = [0, 0.0, 0.0, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0]
grade3 = [0, 0.0, 0.0, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0]
review3 = [0.0, 0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.8, 0.7]
Result3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result3[i] = min(max(study3[1], grade3[3]), review3[i])

print(Result3)

reverse_fuzzy = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0, 10):
    reverse_fuzzy[i] = max(max(Result1[i], Result2[i]), Result3[i])

print(reverse_fuzzy)

T1 = 0
T2 = 0

for i in range(0, 10):
    T1 += i * reverse_fuzzy[i]
    T2 += reverse_fuzzy[i]

print(T1)
print(T2)
T3 = round(T1 / T2)
print(reverse_fuzzy[T3])
