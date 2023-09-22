n = int(input())

Regular = set()
VIP_codes = set()

for _ in range(n):
    code = input()
    if code[0].isnumeric():
        VIP_codes.add(code)
    else:
        Regular.add(code)

# print(VIP_codes)
# print(Regular)
guest = input()
while guest != "END":

    if guest in VIP_codes:
        VIP_codes.remove(guest)
    elif guest in Regular:
        Regular.remove(guest)

    guest = input()
print(len(VIP_codes) + len(Regular))
print('\n'.join(sorted(VIP_codes)))
print('\n'.join(sorted(Regular)))
