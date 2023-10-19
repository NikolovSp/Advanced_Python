def area(length, width):
    return f'Rectangle area: {length * width}\n'


def perimeter(length, width):
    return f'Rectangle perimeter: {2 * (length + width)}'


def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f'Enter valid values!'
    result = ''
    result += area(length, width)
    result += perimeter(length, width)
    return result


print(rectangle(2, 10))
print(rectangle('2', 10))
