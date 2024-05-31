fruitage1 = [1, 0.9, 0.9, 0.8, 0.7, 0.5, 0.2, 0.1, 0.05]
skill1 = [1, 0.9, 0.9, 0.8, 0.6, 0.3, 0.2, 0.1, 0.1, 0.01]
Salary1 = [0.2, 0.3, 0.5, 0.7, 0.5, 0.3, 0.3, 0.2, 0.2, 0.0]
Result1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result1[i] = min(max(fruitage1[1], skill1[6]), Salary1[i])

print(Result1)

fruitage2 = [0, 0.2, 0.3, 0.4, 0.5, 1.0, 0.5, 0.4, 0.3, 0.2]
Salary2 = [0.0, 0.0, 0.2, 0.3, 0.5, 1.0, 0.5, 0.3, 0.2, 0.0]
Result2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result2[i] = min(fruitage2[1], Salary2[i])

print(Result2)

fruitage3 = [0, 0.1, 0.2, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0]
skill3 = [0, 0.0, 0.2, 0.4, 0.4, 0.5, 0.6, 0.7, 0.9, 1.0]
Salary3 = [0.0, 0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.0]
Result3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(0, 10):
    Result3[i] = min(max(fruitage3[1], skill3[6]), Salary3[i])

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
