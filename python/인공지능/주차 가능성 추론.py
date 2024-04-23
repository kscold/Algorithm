# 규칙 #1: IF 주차 가능한 공간의 크기가 50대이다. & 주차를 할 수 있다. THEN 주차장에 주차를 했다.
# 규칙 #2: IF 주차장에 차가 25대 이상 차 있다. THEN 주차장이 절반 이상 차 있다.
# 규칙 #3: IF 지금 주차 공간을 찾고 있다. & IF 주차장 절반 이상이 차 있다. THEN 주차를 할 수 있다.

symbol = {"A": "주차 가능한 공간의 크기가 50대이다.", "B": "주차를 할 수 있다.", "C": "주차장에 주차를 했다", "D": "주차장에 차가 25대 이상 차 있다.",
          "E": "주차장이 절반 이상 차 있다.", "F": "지금 주차 공간을 찾고 있다."}


def parking_expert(short):
    if "A" in short and "B" in short:
        short.append("C")
    if "D" in short:
        short.append("E")
    if "F" in short and "E" in short:
        short.append("B")


def reverse_parking_expert(short, n):
    if n == 0 and "A" in short and "B" in short:
        short.append("C")
    if n == 1 and "D" in short:
        short.append("E")
    if n == 2 and "F" in short and "E" in short:
        short.append("B")


# 주차 가능한 공간의 크기가 50대이다.
# 주차장에 차가 25대 이상 차 있다.
# 지금 주차 공간을 찾고 있다.

short = ["A", "D", "F"]
print(short)

parking_expert(short)
parking_expert(short)

if "C" in short:
    print(symbol["C"])

Open = (1, 2, 0)
for i in Open:
    reverse_parking_expert(short, i)

print(i, short)

if "C" in short:
    print(symbol["C"])
