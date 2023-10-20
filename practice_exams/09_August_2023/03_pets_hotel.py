def accommodate_new_pets(capacity, max_weight, *args):
    pets_dict = {}
    full = True
    for pet, pet_weight in args:
        if capacity == 0:
            full = False
            break
        if pet_weight > max_weight:
            continue

        if pet not in pets_dict:
            pets_dict[pet] = 0
        pets_dict[pet] += 1
        capacity -= 1

    result = []
    if full:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")
    else:
        result.append(f"You did not manage to accommodate all pets!")
    result.append(f"Accommodated pets:")
    for k, v in sorted(pets_dict.items()):
        result.append(f"{k}: {v}")
    return "\n".join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
