expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ')':
        starting_index = stack.pop()
        print(expression[starting_index:index + 1])
