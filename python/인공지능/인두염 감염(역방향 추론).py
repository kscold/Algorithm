# 규칙 #1: IF 목이 부어있다. & 감염이 의심된다. THEN 환자는 인두염이다.
# 규칙 #2: IF 체온이 38도 이상이다. THEN 열이 있다.
# 규칙 #3: IF 환자가 한달 이상 아프다. & 열이 있다. THEN 감염이 의심된다.

symbol = {"A": "목이 부음", "B": "감염", "C": "인두염", "D": "체온이 38도", "E": "열", "F": "환자가 한달 이상 아픔"}


def cold_expert(short, n):
    if n == 0 and "A" in short and "B" in short:
        short.append("C")
    if n == 1 and "D" in short:
        short.append("E")
    if n == 2 and "F" in short and "E" in short:
        short.append("B")


short = ["D", "F", "A"]
Open = (1, 2, 0)
for i in Open:
    cold_expert(short, i)

# 환자의 체온이 38도이다.
# 환자가 2달 동안 아팠다.
# 환자의 목이 부어있다.


print(i, short)

if "C" in short:
    print(symbol["C"])
