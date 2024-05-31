amount1 = [1, 0.95, 0.9, 0.8, 0.8, 0.65, 0.6, 0.5, 0.25, 0.1, 0.05] # 세탁물 양
pollution1 = [1, 1, 0, 0.95, 0.9, 0.7, 0.4, 0.25, 0.2, 0.2, 0.1] # 오염도
time1 = [0.0, 0.01, 0.2, 0.25, 0.4, 0.6, 1.0, 0.7, 0.3, 0.2, 0.1] # 시간
Result1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result1[i] = min(max(amount1[1], pollution1[6]), time1[i]) # 0.95 0.25

print(Result1)

amount2 = [0, 0.1, 0.2, 0.3, 0.55, 0.9, 0.6, 0.5, 0.35, 0.1]
time2 = [0.0, 0.01, 0.2, 0.3, 0.5, 1.0, 0.65, 0.4, 0.2, 0.1]
Result2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result2[i] = min(amount2[2], time2[i])

print(Result2)

amount3 =[0.0, 0.01, 0.02, 0.2, 0.35, 0.4, 0.45, 0.7, 0.85, 1.0]
pollution3 = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.7, 0.75, 0.9, 0.95]
time3 = [0.0, 0.0, 0.15, 0.25, 0.3, 0.5, 0.55, 0.7, 1.0, 0.8, 0.65]
Result3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result3[i] = min(max(amount3[1], pollution3[6]), time3[i])

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
