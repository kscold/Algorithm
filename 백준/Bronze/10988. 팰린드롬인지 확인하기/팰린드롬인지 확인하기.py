def words_reverse(words):
    str_reverse = ""
    for word in words:
        str_reverse = word + str_reverse

    return str_reverse


words = input()

if words == words_reverse(words):
    print(1)
else:
    print(0)