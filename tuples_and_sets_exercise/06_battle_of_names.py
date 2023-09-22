n = int(input())

current_row = 0
even_names = set()
odd_names = set()


for _ in range(n):
    current_row += 1
    sum_asci_values = 0
    name = input()
    for ch in name:
        sum_asci_values += ord(ch)
    sum_asci_values = sum_asci_values // current_row
    if sum_asci_values % 2 == 0:
        even_names.add(sum_asci_values)
    else:
        odd_names.add(sum_asci_values)
sum_even = sum(even_names)
sum_odd = sum(odd_names)

if sum_even == sum_odd:
    results = odd_names.union(even_names)
    print(', '.join(map(str, results)))
elif sum_odd > sum_even:
    results = odd_names.difference(even_names)
    # print(', '.join(map(str, results)))
    print(*(odd_names.difference(even_names)), sep=',')
else:
    results = odd_names.symmetric_difference(even_names)
    print(', '.join(map(str, results)))
