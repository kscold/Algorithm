sum_list = []
sub_list = []
for i in range(2, 101):
    if i % 2 == 1:
        sum_list.append(i)

count = 0
for j in sum_list:
    sub_list.append(j)

    for i in range(1, 11):
        if len(sub_list) == int(str(i) + "0"):
            print(sub_list[count:count + 10])
            count += 10
