n, m = [int(x) for x in input().split()]
n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
# input could be int, but would make printing harder. Comparing a set is same for both int/string elements
for _ in range(m):
    m_set.add(input())

print('\n'.join(n_set & m_set)) # print(n_set.intersection(m_set))
