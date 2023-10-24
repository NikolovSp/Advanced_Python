from collections import deque
items_dict = {}
textiles = deque(int(x) for x in input().split())
medicament = [int(x) for x in input().split()]

products = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}

while textiles and medicament:
    curr_textile = textiles.popleft()
    curr_medicament = medicament.pop()
    curr_sum = curr_textile + curr_medicament

    if curr_sum in products:
        if products[curr_sum] not in items_dict:
            items_dict[products[curr_sum]] = 0
        items_dict[products[curr_sum]] += 1

    elif curr_sum > 100:
        if 'MedKit' not in items_dict:
            items_dict['MedKit'] = 0
        items_dict['MedKit'] += 1

        curr_sum -= 100
        medicament[-1] += curr_sum

    else:
        curr_medicament += 10
        medicament.append(curr_medicament)
both_finished = False
if not medicament and not textiles:
    print("Textiles and medicaments are both empty.")
    both_finished = True
elif not medicament:
    print("Medicaments are empty.")
    result = f"Textiles left: {', '.join([str(el) for el in textiles])}"
else:
    print("Textiles are empty.")
    result = f"Medicaments left: {', '.join([str(el) for el in medicament[::-1]])}"

ordered_dict = dict(sorted(items_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])))
[print(f"{item_name} - {amount_created}") for item_name, amount_created in ordered_dict.items()]
if not both_finished:
    print(result)
