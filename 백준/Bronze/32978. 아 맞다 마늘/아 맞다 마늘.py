N = int(input())
ingredients = input().split()
used = input().split()

for i in range(len(used)):
    ingredients.remove(used[i])

print(ingredients[0])