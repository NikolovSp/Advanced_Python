presents = {150: ['Doll', 0], 250: ['Wooden train', 0], 300:['Teddy Bear', 0], 400:['Bicycle', 0]}
toys_made = {}
# for name in presents.values():
#     toys_made[name[0]] = name[1]
# print(toys_made)

toys_made = {name[0]: name[1] for name in sorted(presents.values())}
print(toys_made)