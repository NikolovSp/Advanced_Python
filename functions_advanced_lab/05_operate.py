from functools import reduce


def add(*args):
    return reduce(lambda a, b: a + b, args)


def substract(*args):
    return reduce(lambda a, b: a - b, args)


def multiply(*args):
    return reduce(lambda a, b: a * b, args)


def division(*args):
    return reduce(lambda a, b: a / b, args)


mapper = {'+': add,
          '-': substract,
          '*': multiply,
          '/': division
          }


def operate(operator, *args):
    return mapper[operator](*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
