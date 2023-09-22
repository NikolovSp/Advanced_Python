from math import floor
from collections import deque

operators = ['*', '/', '+', '-']
expression = deque(input().split())
last_digits = deque()

for char in expression:
    if char not in operators:
        last_digits.append(int(char))
    else:
        current_result = last_digits.popleft()
        while last_digits:
            if char == operators[0]:
                current_result *= last_digits.popleft()
            elif char == operators[1]:
                current_result = floor(current_result / last_digits.popleft())
            elif char == operators[2]:
                current_result += last_digits.popleft()
            else:
                current_result -= last_digits.popleft()

        last_digits.appendleft(current_result)
print(*last_digits)
