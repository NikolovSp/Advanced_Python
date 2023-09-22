n = int(input())

guest_list = set()

for _ in range(n):
    reservation_number = input()
    guest_list.add(reservation_number)

guest = input()
while guest != 'END':
    guest_list.remove(guest)
    guest = input()

print(len(guest_list))
for num in sorted(guest_list):
    print(num)
