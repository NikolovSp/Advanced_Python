from collections import deque

fuel = [int(x) for x in input().split()]
cons_index = deque(int(x) for x in input().split())
altitude = deque(int(x) for x in input().split())

altitude_counter = 0
top = True
while altitude:
    altitude_counter += 1
    curr_fuel = fuel.pop()
    curr_index = cons_index.popleft()
    total_fuel = curr_fuel - curr_index
    if total_fuel >= altitude[0]:
        print(f'John has reached: Altitude {altitude_counter}')
        altitude.popleft()

    else:
        print(f'John did not reach: Altitude {altitude_counter}')
        print('John failed to reach the top.')
        altitude_counter -= 1
        top = False
        break

else:
    print('John has reached all the altitudes and managed to reach the top!')

if not top and altitude_counter > 1:
    formated_altitudes = []
    for i in range(1, altitude_counter + 1):
        formated_altitudes.append(f"Altitude {i}")

    print(f'Reached altitudes: {", ".join(formated_altitudes)}')
else:
    print("John failed to reach the top. John didn't reach any altitude.")
    