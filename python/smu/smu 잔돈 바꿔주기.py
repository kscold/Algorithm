# 잔돈 바꿔주기
# 상명이는 새로운 가게를 차렸다. 팔려는 물건은 $5 짜리이다. 그런데, 새로 가게를 차려서 가게를 오픈했을 때 잔돈이
# 하나도 없다. 손님이 내는 지폐가 배열로 주어졌을 때 상명이는 모든 손님에게 잔돈을 바꿔줄 수 있을지 계산하는
# 함수를 작성하시오.

# 예시)
# 입력
# 2 // 총 2 개의 입력
# 5 5 5 5 10 20 // 5 명의 손님, 각각 $5, $5, $5, $10, $20 불 지폐로 계산
# 5 5 5 10 10 20 // 5 명의 손님, 각각 $5, $5, $10, $10, $20 불 지폐로 계산

# 출력
# True
# False

def can_give_change(customers):
    five_count = 0
    ten_count = 0

    for payment in customers:
        payment_value = payment

        if payment_value == 5:
            five_count += 1
        elif payment_value == 10:
            if five_count == 0:
                return False
            five_count -= 1
            ten_count += 1
        elif payment_value == 20:
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False

    return True


# 입력
n = int(input())
data = []
for _ in range(n):
    payments = map(int, input().split()[1:])
    data.append(payments)

# 결과 출력
for customers in data:
    result = can_give_change(customers)
    print(str(result))

# 2
# 5 5 5 5 10 20
# 5 5 5 10 10 20
