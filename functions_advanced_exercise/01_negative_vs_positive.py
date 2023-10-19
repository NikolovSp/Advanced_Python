def sum_nums(*args):

    negative_ = 0
    positive_ = 0
    for num in args:
        if num < 0:
            negative_ += num
        else:
            positive_ += num
    return negative_, positive_


numbers = [int(x) for x in input().split()]
negative, positive = sum_nums(*numbers)

print(negative)
print(positive)
if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
