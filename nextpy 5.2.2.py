# 5.2.2
################

numbers = iter(list(range(1, 101)))
for i in numbers:
    try:
        next(numbers)
        next(numbers)
        print(i)
    except StopIteration:
        print('No more numbers')