from collections import deque

queue = deque()
name = input()
while name != "End":
    if name == "Paid":
        print("\n".join(queue))
        queue.clear()
    else:
        queue.append(name)

    name = input()
print(f"{len(queue)} people remaining.")
