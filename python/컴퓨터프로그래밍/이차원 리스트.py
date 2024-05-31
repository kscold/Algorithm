datas = [[1, "김진희"], [2, "김서영"], [3, "김승찬"], [4, "성지훈"]]

tmp = []
while True:
    n = int(input("동작을 입력하세요"))

    if n == 1:
        print("검색된 데이터")
        for data in datas:
            for i in data:
                print(f"{i} ", end="")
            print()

    elif n == 2:
        print("데이터를 추가합니다.")
        tmp.append(list(map(str, input().split())))
        datas.extend(tmp)
        print(datas)

    elif n == 3:
        if len(datas) <= 0:
            print("더 이상 삭제할 데이터가 없습니다.")
            continue
        print("가장 마지막 데이터를 삭제합니다.")
        datas.pop()
        print(datas)

    else:
        break
