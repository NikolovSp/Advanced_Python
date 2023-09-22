n = int(input())

chemical_elements = set()

for _ in range(n):
    elements = input().split()
    for i in range(len(elements)):
        chemical_elements.add(elements[i])
#   for el in elements:

print('\n'.join(chemical_elements))
