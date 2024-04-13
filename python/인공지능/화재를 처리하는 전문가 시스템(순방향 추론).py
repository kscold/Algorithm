def fire_expert(short):
    if "B" in short and "C" in short:
        short.append("D")
    if "A" in short:
        short.append("C")
    if "D" in short:
        short.append("E")


short = ["A", "B"]
print(short)

fire_expert(short)
if "E" in short:
    print("소방서에 신고한다")

fire_expert(short)
if "E" in short:
    print("소방서에 신고한다")
