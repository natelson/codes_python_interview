


def factiorial(number):
    result = number
    for n in range(number-1,0,-1):
        result *=n

    return result


print(factiorial(5))
print(factiorial(0))

print(factiorial(-1))