def even_odd_filter(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        if k == 'odd':
            new_dict[k] = list(filter(lambda v: v % 2 != 0, kwargs[k]))
        else:
            new_dict[k] = list(filter(lambda v: v % 2 == 0, kwargs[k]))

    # sorted_dict = dict(sorted(new_dict.items(), key=lambda kvp: len(kvp[1]), reverse=True))
    return dict(sorted(new_dict.items(), key=lambda kvp: len(kvp[1]), reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print()
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

