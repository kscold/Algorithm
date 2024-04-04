# a, b = input().split()
# a, b = float(a), float(b)
#
# result = (a + b) / 2
# wrapperResult = round(result, 2)
#
# if result > 70:
#     print("합격")
# else:
#     print("불합격")
#
# print(f"평균점수: {wrapperResult}")


result = list(map(float, input().split()))

error_count = 0
for i in result:
    if 100 < i:
        error_count += 1

if error_count == 0:
    result = sum(result) / 3
    if 90 <= result and result <= 100:
        print("A")
    elif 80 <= result and result < 90:
        print("B")
    elif 70 <= result and result < 80:
        print("C")

    else:
        print("F")
else:
    print(f"{error_count}개의 숫자가 올바르지 않습니다.")
