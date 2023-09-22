stack = []

n = int(input())
for i in range(n):
    command = input().split()
    if len(command) == 2:
        stack.append(int(command[1]))
    # print(stack)
    if command[0] == '2':
        stack.pop()
    if command[0] == '3':
        top_element = max(stack)
        print(top_element)
    if command[0] == '4':
        min_value = min(stack)
        print(min_value)

while stack:
    print(stack.pop(), end='')
    if stack:
        print(', ', end='')
