n = int(input())

result = n
for i in range(n - 1, 1, -1):
    result = result * i

print(f"{n}! = ", end="")

for i in range(n, 1,-1):
    print(f"{i} * ", end="")

print("1 = ", end="")
print(result)


# def factorial_recursive(n):
#     return n * factorial_recursive(n - 1) if n > 1 else 1
#
#
# print(factorial_recursive(n))
