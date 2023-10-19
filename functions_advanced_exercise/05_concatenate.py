def concatenate(*args, **kwargs):
    result = ''
    for word in args:
        result += word
    for k, v in kwargs.items():
        if k in result:
            result = result.replace(k, v)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print()
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))