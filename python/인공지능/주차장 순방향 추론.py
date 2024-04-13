# 규칙 #1: IF 주차장의 크기가 50대이다. & 주자장에 차가 25대 이상이다. THEN 주차장이 절반 이상 차 있다.
# 규칙 #2: IF 주차장에 차가 25대 이상이다. THEN 주차장에 공간이 있다.
# 규칙 #3: IF 주차장에 공간이 있다. & IF 주차장 절반 이상이 차 있다. THEN 주차를 할 수 있다.

symbol = {"A": "주차 가능한 공간이 50대인 주차장이 있다.", "B": "주차장에 차가 25대 이상있다.", "C": "주차장이 절반 이상 차 있다.", "D": "주차장에 공간이 있다.",
          "E": "주차를 할 수 있다."}


def parking_expert(short):
    if "A" in short and "B" in short:
        short.append("C")
    if "B"  in short:
        short.append("D")
    if "D" in short and "C" in short:
        short.append("E")


# 주차 가능한 공간이 50대인 주차장이 있다.
# 주차장에 차가 25대가 있이고 주차장에 공간이 있다.

short = ["A", "B"]
print(short)

parking_expert(short)
if "E" in short:
    print(symbol["E"])