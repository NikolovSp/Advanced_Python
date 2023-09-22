numbers = [int(num) for num in input().split()]
queue = []
# print(numbers)
while numbers:
    # print(numbers.pop(), end=" ")
    queue.append(numbers.pop())
print(*queue, end=" ")
