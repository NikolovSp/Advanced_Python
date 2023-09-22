from collections import deque

n = int(input())
pumps = deque()
start_position = 0
stops_counter = 0

for _ in range(n):
    current_petrol, distance_to_next_pump = input().split()
    pumps.append([int(current_petrol), int(distance_to_next_pump)])
# print(pumps)

while stops_counter < n:
    total_petrol = 0
    for i in range(n):
        total_petrol += pumps[i][0]
        destination = pumps[i][1]
        if total_petrol < destination:
            pumps.rotate(-1)
            start_position += 1
            stops_counter = 0
            break
        total_petrol -= destination
        stops_counter += 1

print(start_position)
