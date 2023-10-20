from collections import deque

time = deque(int(x) for x in input().split())
tasks = [int(x) for x in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}
while time and tasks:
    current_time = time.popleft()
    current_task = tasks.pop()
    score = current_task * current_time

    if 0 < score <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 60 < score <= 120:
        ducks["Thor Ducky"] += 1
    elif 120 < score <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 180 < score <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        current_task -= 2
        time.append(current_time)
        tasks.append(current_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for k,v in ducks.items():
    print(f"{k}: {v}")
