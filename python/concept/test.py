jdg = 0
for i in range(5):
    num = input("학번: ")
    com, data = input("컴퓨팅 사고, 데이터분석 점수 입력").split(",")
    com, data = int(com), int(data)
    avg = (com + data) / 2
    if avg >= 90:
        jdg = jdg + 1
    print(f"평균: {avg:.2f}점, 판정: {'합격' if avg >= 90 else '불합격'}")
print("*" * 40)
print(f"합격자 수 {jdg} 명")
