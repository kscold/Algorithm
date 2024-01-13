def fun1(A, B, C):
    return (A + B) % C


def fun2(A, B, C):
    return ((A % C) + (B % C)) % C


def fun3(A, B, C):
    return (A * B) % C


def fun4(A, B, C):
    return ((A % C) * (B % C)) % C


a, b, c = map(int, input().split())
print(fun1(a, b, c))
print(fun2(a, b, c))
print(fun3(a, b, c))
print(fun4(a, b, c))