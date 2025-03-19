N, M = map(int, input().split())
pokemons = {}
pokemons_lst = []
for idx in range(1, N + 1):
    pokemon = input()
    pokemons[pokemon] = idx
    pokemons_lst.append(pokemon)

for i in range(M):
    query = input()
    if query.isdigit():
        print(pokemons_lst[int(query) - 1])
    else:
        print(pokemons[query])