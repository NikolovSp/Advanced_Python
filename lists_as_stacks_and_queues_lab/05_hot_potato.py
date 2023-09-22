from collections import deque

name = list(input().split())
queue = deque(name)
# queue.rotate(-2)
# print(queue)

n = int(input())

while len(queue) != 1:
    queue.rotate(-n + 1)
    print(f'Removed {queue.popleft()}')
print(f'Last is {queue.popleft()}')
