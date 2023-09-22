from collections import deque
result = ''
quantity_of_food = int(input())
orders = deque([int(a) for a in input().split()])
# deque([20, 54, 30, 16, 7, 9])
max_order = max(orders)
Food = True
while orders:
    current_order = orders.popleft()
    if current_order >= quantity_of_food:
        orders.appendleft(current_order)
        Food = False
        break
    else:
        quantity_of_food -= current_order


print(max_order)
if Food:
    print('Orders complete')
else:
    print('Orders left: ', end='')
    while orders:
        print(orders.popleft(), end="")
        if orders:
            print(' ', end='')
    # while orders:
    #     result += f"{str(orders.popleft())} "
    # print(f'Orders left: {result}')
