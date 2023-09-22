sentence = input()

count = {}

for char in range(len(sentence)):
    if sentence[char] not in count:
        count[sentence[char]] = 0
    count[sentence[char]] += 1
sorted_count = {key: value for key, value in sorted(count.items())}

for char, count in sorted_count.items():
    print(f'{char}: {count} time/s')
