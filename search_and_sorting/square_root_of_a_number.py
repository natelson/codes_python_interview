def find_square(number):
    if number == 0 or number == 1:
        return number

    for i in range(number):
        result = i * i
        if (i * i) == number:
            return i

        if result > number:
            return i - 1

    return 1

assert 1 == find_square(1)
assert 1 == find_square(2)
assert 2 == find_square(4)
assert 3 == find_square(9)
