def reverse(target):
    reverse_str = ""
    for i in target:
        reverse_str = i + reverse_str

    return int(reverse_str)


a, b = map(str, input().split())


if reverse(a) > reverse(b):
    print(reverse(a))
else:
    print(reverse(b))