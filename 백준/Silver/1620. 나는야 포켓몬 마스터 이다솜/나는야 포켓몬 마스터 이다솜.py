n, m = map(int, input().split())
pokemons = [input().strip() for _ in range(n)]
questions = [input().strip() for _ in range(m)]

pokemon_dict = {}
for i, pokemon in enumerate(pokemons, 1):
    pokemon_dict[pokemon] = i

for question in questions:
    if question.isdigit():
        print(pokemons[int(question) - 1])
    else:
        print(pokemon_dict[question])