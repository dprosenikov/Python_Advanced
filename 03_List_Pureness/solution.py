def best_list_pureness(*args):
    from collections import deque
    numbers = deque(args[0])
    k = int(args[1])
    counter = 0
    best_pure = 0
    for x in numbers:
        best_pure += int(x) * numbers.index(x)
    for n in range(k):
        numbers.rotate()
        current_pure = 0
        for x in numbers:
            current_pure += int(x) * numbers.index(x)
            if current_pure > best_pure:
                best_pure = current_pure
                counter = n + 1

    return f'Best pureness {best_pure} after {counter} rotations'

# test = ([4, 3, 2, 6], 4)
# test = ([7, 9, 2, 5, 3, 4], 3)
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
