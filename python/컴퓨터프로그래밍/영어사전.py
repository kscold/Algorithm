engDict = {"flower": "꽃", "apple": "사과", "banana": "바나나"}

while True:
    n = int(input("동작을 입력하세요"))

    if n == 1:
        print("검색된 데이터")
        for key in engDict:
            print(engDict[key])

    elif n == 2:
        print("데이터를 추가합니다.")

        engWord, korWord = map(str, input().split())

        if engWord in engDict.keys():
            print("이미 있는 데이터입니다.")
            continue

        engDict[engWord] = korWord

        print(engDict)

    else:
        print("프로그램 종료")
        break