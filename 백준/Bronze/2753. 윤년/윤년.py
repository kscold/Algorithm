def yearResult(preyear):
    if (preyear % 4 == 0 and preyear % 100 != 0) or preyear % 400 == 0:
        return 1
    return 0


preyear = int(input())
result = yearResult(preyear)
print(result)