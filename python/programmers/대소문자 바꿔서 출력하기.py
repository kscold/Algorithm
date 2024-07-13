str = input()

result = []
for c in str:
    if c.islower():
        result.append(c.upper())
    else:
        result.append(c.lower())

print("".join(result))

