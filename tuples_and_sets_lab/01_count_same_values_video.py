numbers = tuple(float(x) for x in input().split())

times_seen = {}

for num in numbers:
    if num not in times_seen:
        times_seen[num] = numbers.count(num)

for key, value in times_seen.items():
    print(f'{key:.1f} - {value} times')
