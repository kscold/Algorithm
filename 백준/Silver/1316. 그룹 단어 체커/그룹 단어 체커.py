n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

count = 0

for string in strings:
    char_set = set()
    is_group_word = True

    for char in string:
        if char in char_set and char != prev_char:
            is_group_word = False
            break

        char_set.add(char)
        prev_char = char

    if is_group_word:
        count += 1

print(count)