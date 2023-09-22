from collections import deque

starting_water = int(input())
people_list = deque()

while True:
    name = input()
    if name == "Start":
        break
    people_list.append(name)
# print(people_list)
while True:
    command = input()
    if command == "End":
        print(f"{starting_water} liters left")
        break

    if 'refill' in command:
        command = command.split()
        starting_water += int(command[1])
    else:
        command = int(command)
        if starting_water >= command:
            print(f"{people_list.popleft()} got water")
            starting_water -= command
        else:
            print(f"{people_list.popleft()} must wait")
