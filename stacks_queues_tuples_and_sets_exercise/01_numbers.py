a_set = set(int(x) for x in input().split())
b_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'Add' and command[1] == 'First':
        for i in range(2, len(command)):
            a_set.add(int(command[i]))
    elif command[0] == 'Add' and command[1] == 'Second':
        for i in range(2, len(command)):
            b_set.add(int(command[i]))
    elif command[0] == 'Remove' and command[1] == 'First':
        for i in range(2, len(command)):
            a_set.difference_update(command[i])
    elif command[0] == 'Remove' and command[1] == 'Second':
        for i in range(2, len(command)):
            b_set.difference_update(command[i])
    else:
        if a_set.issubset(b_set) or b_set.issubset(a_set):
            print(True)
        else:
            print(False)

print(*a_set, sep=', ')
print(*b_set, sep=', ')
