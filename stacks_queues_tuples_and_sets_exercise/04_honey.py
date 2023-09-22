from math import sqrt
from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey_made = 0

while bees and nectar:

    if bees[0] <= nectar[-1]:
        matched_bee = bees.popleft()
        matched_nectar = nectar.pop()
        current_symbol = symbols.popleft()
        if current_symbol == '+':
            total_honey_made += (matched_bee + matched_nectar)
        elif current_symbol == '-':
            total_honey_made += abs(matched_bee - matched_nectar)
        elif current_symbol == '*':
            total_honey_made += (matched_bee * matched_nectar)
        elif current_symbol == '/':
            if matched_nectar == 0:
                continue
            else:
                total_honey_made += (matched_bee / matched_nectar)

    else:
        nectar.pop()

print(f'Total honey made: {total_honey_made}')
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
