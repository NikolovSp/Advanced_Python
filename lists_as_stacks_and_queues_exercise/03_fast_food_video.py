from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])
# print(orders)

print(max(orders))

while orders and orders[0] <= quantity_of_food:
    quantity_of_food -= orders[0]
    orders.popleft()

if orders:
    print('Orders left:', end='')
    while orders:
        print(f' {orders.popleft()}', end='')
else:
    print('Orders complete')
