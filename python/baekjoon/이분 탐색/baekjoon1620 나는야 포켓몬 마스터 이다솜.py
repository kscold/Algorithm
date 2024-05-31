n, m = map(int, input().split())
pokemons = [input().strip() for _ in range(n)]
questions = [input().strip() for _ in range(m)]

pokemon_dict = {}
for i, pokemon in enumerate(pokemons, 1):
    pokemon_dict[pokemon] = i

for question in questions:
    if question.isdigit(): # 만약 문자로 변환가능한 숫자이면
        print(pokemons[int(question) - 1])
    else:
        print(pokemon_dict[question])

# def binary_search(pokemons, target):
#     start = 0
#     end = len(pokemons) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if pokemons[mid][0] == target:
#             return pokemons[mid][1]
#         elif pokemons[mid][0] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return None
#
#
# n, m = map(int, input().split())
# pokemons = [input().strip() for _ in range(n)]
# pokemons_sorted = sorted((pokemon, i + 1) for i, pokemon in enumerate(pokemons))
#
# for _ in range(m):
#     question = input().strip()
#     if question.isdigit():
#         index = int(question)
#         print(pokemons[index - 1])
#     else:
#         result = binary_search(pokemons_sorted, question)
#         print(result)
