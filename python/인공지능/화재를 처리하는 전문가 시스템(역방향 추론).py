def fire_expert_rules(short, n):
    if n == 0 and "B" in short and "C" in short:
        short.append("D")
    if n == 1 and "A" in short:
        short.append("C")
    if n == 2 and "D" in short:
        short.append("E")


short = ["A", "B"]
Open = (1, 0, 2)
for i in Open:
    fire_expert_rules(short, i)

print(i, short)
if "E" in short:
    print("소방서에 신고한다")
