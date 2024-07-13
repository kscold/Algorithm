words = input()
words = words.upper()
set_list = list(set(words))

set_count = []
for i in set_list:
    set_count.append(words.count(i))

if set_count.count(max(set_count)) > 1:
    print("?")
else:
    print(set_list[set_count.index(max(set_count))])