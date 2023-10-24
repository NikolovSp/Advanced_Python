from collections import deque

initial_fuel = [int(x) for x in input().split()]
index = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

altitude_counter = 0
altitudes = []
for _ in range(4):
    altitude_counter += 1
    current_fuel = initial_fuel.pop()
    current_index = index.popleft()

    total_fuel = current_fuel - current_index

    if total_fuel >= fuel_needed[0]:
        print(f"John has reached: Altitude {altitude_counter}")
        altitudes.append(f"Altitude {altitude_counter}")
        fuel_needed.popleft()
    else:
        print(f"John did not reach: Altitude {altitude_counter}")
        break

else:
    print("John has reached all the altitudes and managed to reach the top!")
    exit()

if altitudes:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(altitudes)}")
else:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
