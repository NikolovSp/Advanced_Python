def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    print(sorted_dict)
    result = []
    for kvp in sorted_dict:
        result.append(kvp[0])
        result += sorted(kvp[1], reverse=True)

    return '\n'.join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
