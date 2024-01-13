target = int(input())
sub = input()

reverse_sub = []
for s in sub:
    reverse_sub.append(s)

result_list = []
for ssub in reverse_sub[::-1]:
    result_list.append(int(ssub) * target)

result_list.append(target * int(sub))

for result in result_list:
    print(result)