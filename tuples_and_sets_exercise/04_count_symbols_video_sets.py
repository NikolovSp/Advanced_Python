txt = tuple(input())

unique_symbols = sorted(set(txt))

for element in unique_symbols:
    print(f'{element}: {txt.count(element)} time/s')
# a bit slower operation because count goes over the list for each element
