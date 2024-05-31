def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return float(a / b)


# 심볼 감지
def symbolDetection(symbol):
    if symbol == "+":
        print(sum(a, b))
    elif symbol == "-":
        print(sub(a, b))
    elif symbol == "*":
        print(mul(a, b))
    elif symbol == "/":
        print(div(a, b))
    else:
        print("잘못된 기호입니다.")


# 유동적인 경우를 감지하기 위해 map(int, input().split())을 사용하지 않았음
def inputDetectrion(datas):
    # if len(datas) == 3:
    #     a = datas[0]
    #     b = datas[2]
    #     symbol = datas[1]
    #     return a, b, symbol
    #
    # if len(datas) == 4:
    #     if data[1] == " ":
    #         a = datas[0]
    #         b = datas[3]
    #         symbol = datas[2]
    #         return a, b, symbol
    #     elif data[2] == " ":
    #         a = datas[0]
    #         b = datas[3]
    #         symbol = datas[1]
    #         return a, b, symbol
    # elif len(datas) == 5:
    #     a = datas[0]
    #     b = datas[4]
    #     symbol = datas[2]
    #     return a, b, symbol

    if len(datas) > 0:
        data = list(map(str, datas))

        for i in data:
            if data == " ":
                data.pop(data.index(i))
                print(data)


        return data[0], data[2], data[1]
    else:
        return 0


data = input()

if inputDetectrion(data) == 0:
    print("잘못된 입력입니다.")

a, b, symbol = inputDetectrion(data)

a, b = int(a), int(b)
symbolDetection(symbol)
