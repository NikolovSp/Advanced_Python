from collections import deque

name = list(input().split())
children = deque(name)
n = int(input())
while len(children) > 1:
    for rotations in range(n - 1):
        kid_to_rotate = children.popleft()
        children.append(kid_to_rotate)
    print(f'Removed {children.popleft()}')
print(f"Last is {children.popleft()}")
