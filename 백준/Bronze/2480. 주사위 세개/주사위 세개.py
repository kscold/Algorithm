a, b, c = map(int, input().split())
data = []
count = []
real_value = []

if a == b and b == c and a == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    data.append(a)
    data.append(b)
    data.append(c)
    for i in data:
        if i not in count:
            count.append(i)
        else:
            if i not in real_value:
                real_value.append(i)
    print(1000 + real_value[0] * 100)
elif a != b and b != c and a != c:
    data.append(a)
    data.append(b)
    data.append(c)
    data.sort(reverse=True)
    print(data[0] * 100)