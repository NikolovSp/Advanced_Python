parentheses = input()

bracets = []
square = []
wings = []

for i in range(len(parentheses)):
    if parentheses[i] == '(':
        bracets.append(i)
    elif parentheses[i] == '[':
        square.append(i)
    else:
        wings.append(i)

    if parentheses[i] == ')':

