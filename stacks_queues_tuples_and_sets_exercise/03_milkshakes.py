from collections import deque

chocolate = [int(x) for x in input().split(',')]
cups_of_milk = deque([int(x) for x in input().split(',')])
prepared_chocolates = 0
# print(chocolate)
# print(cups_of_milk)

while chocolate and prepared_chocolates < 5:
    current_choco = chocolate[-1]
    current_cup = cups_of_milk[0]
    if current_choco <= 0:
        chocolate.pop()
    while current_choco > 0:
        if current_choco == current_cup:
            chocolate.pop()
            cups_of_milk.popleft()
            prepared_chocolates += 1
            break
        else:
            current_choco -= 5
            cups_of_milk.rotate(-1)

print(f"Chocolate: {chocolate}")
print(f"Milk: {cups_of_milk}")

