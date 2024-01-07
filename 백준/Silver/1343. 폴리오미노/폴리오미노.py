boards = input()

data = ["AAAA", "BB"]

result = []

i = 0
while i < len(boards):
    if boards[i:i + 4] == "XXXX":
        result.append(data[0])
        i += 4

    elif boards[i:i + 2] == "XX":
        result.append(data[1])
        i += 2
    elif boards[i] == "X":
        result = ["-1"]
        break
    else:
        result.append(boards[i])
        i += 1

print(''.join(result))