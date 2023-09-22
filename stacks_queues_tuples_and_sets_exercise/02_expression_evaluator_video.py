from collections import deque

expression = input().split()
numbers = deque()

# another option to solve the problem without any if statements
operator = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,

}

for char in expression:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            # if char == "+":
            #     numbers.appendleft(first_number + second_number)
            # elif char == '-':
            #     numbers.appendleft(first_number - second_number)
            # elif char == '*':
            #     numbers.appendleft(first_number * second_number)
            # elif char == '/':
            #     numbers.appendleft(first_number // second_number)
            numbers.appendleft(operator[char](first_number, second_number))

print(*numbers)
