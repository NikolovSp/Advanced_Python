n = int(input())

parking_lot = set()
EMPTY = False
for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.discard(car_number)
        if len(parking_lot) == 0:
            print("Parking Lot is Empty")
            EMPTY = True
            break
if not EMPTY:
    print('\n'.join(parking_lot))
