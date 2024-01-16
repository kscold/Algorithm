string = list(map(str, input()))
count = 0
init = 3
dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i, dial in enumerate(dials):
    for str in string:
        if str in dial:
            count = count + i
count = count + (init * len(string))

print(count)