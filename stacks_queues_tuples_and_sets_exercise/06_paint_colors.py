from collections import deque

colors_string = deque(input().split())

main_colours = ['red', 'blue', 'yellow']
secondary_colours = {'orange': ['red', 'yellow'],
                     'purple': ['red', 'blue'],
                     'green': ['blue', 'yellow'],
                     }
collected_colours = []

while colors_string:
    first_str = colors_string.popleft()
    last_str = colors_string.pop() if colors_string else ''

    if first_str + last_str in main_colours or first_str + last_str in secondary_colours:
        collected_colours.append(first_str + last_str)
    elif last_str + first_str in main_colours or last_str + first_str in secondary_colours:
        collected_colours.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            colors_string.insert(len(colors_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_string.insert(len(colors_string) // 2, last_str[:-1])

for color in collected_colours:
    if color in secondary_colours:
        for el in secondary_colours[color]:
            if el not in collected_colours:
                collected_colours.remove(color)
                break

print(collected_colours)
