from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {150: ['Doll', 0], 250: ['Wooden train', 0], 300:['Teddy bear', 0], 400:['Bicycle', 0]}

while materials and magic_values:
    if magic_values[0] == 0 and materials[-1] == 0:
        magic_values.popleft()
        materials.pop()
        continue
    if materials[-1] == 0:
        materials.pop()
        continue
    if magic_values[0] == 0:
        magic_values.popleft()
        continue

    current_material = materials.pop()
    current_magic = magic_values.popleft()
    magic_level = current_material * current_magic

    if magic_level in presents.keys():
        presents[magic_level][1] += 1
    else:
        if magic_level < 0:
            magic_level = current_material + current_magic
            materials.append(magic_level)
        else:
            current_material += 15
            materials.append(current_material)

# for name in presents.values():
#     toys_made[name[0]] = name[1]
# print(toys_made)
# an option to get the values of a dict and add them to a new one
toys_made = {name[0]: name[1] for name in sorted(presents.values())}
if toys_made['Doll'] > 0 and toys_made['Wooden train'] > 0 or toys_made['Teddy bear'] > 0 and toys_made['Bicycle'] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for key, value in toys_made.items():
    if value > 0:
        print(f'{key}: {value}')
