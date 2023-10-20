from collections import deque

monster_armor = deque(int(x) for x in (input().split(',')))
soldier_attack = [int(x) for x in (input().split(','))]
monsters_killed = 0
while len(monster_armor) > 0 and len(soldier_attack) > 0:
    attack = soldier_attack.pop()
    armor = monster_armor.popleft()

    if attack >= armor:
        monsters_killed += 1
        attack -= armor
        if soldier_attack:
            soldier_attack[-1] += attack
        elif not soldier_attack and attack > 0:
            soldier_attack.append(attack)

    else:
        armor -= attack
        monster_armor.append(armor)

if not monster_armor:
    print("All monsters have been killed!")
if not soldier_attack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
