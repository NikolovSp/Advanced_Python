n = int(input())

unique_usernames =  set()
for _ in range(n):
    unique_usernames.add(input())
print('\n'.join(unique_usernames))
# print(*unique_usernames, sep='\n')
# same print but could work on list of integers
