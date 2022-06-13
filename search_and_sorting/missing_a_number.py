# John likes to play with numbers and he has N numbers.
# One day he was placing the numbers on the playing board just to
# count that how many numbers he have. He was placing the numbers
# in increasing order i.e. from 1 to N. But when he was putting
# the numbers back into his bag, some numbers fell down onto the
# floor. He picked up all the numbers but one number, he couldn't
# find. Now he have to go somewhere urgently, so he asks you to
# find the missing number.
#
#
# Example 1:
#
# Input:
# N = 4
# A[] = {1, 4, 3}
# Output:
# 2
# Explanation:
# Vaibhav placed 4 integers but he picked
# up only 3 numbers. So missing number
# will be 2 as it will become 1,2,3,4.

def get_missing_numbers(arr, size):
    result = []
    if len(arr) == size:
        return result

    arr = sorted(arr)
    i = 1
    for index in range(0, len(arr)):
        if arr[index] != i:
            result.append(i)

        if len(result) + len(arr) == size:
            return  result

        i+=1

    return result


print(get_missing_numbers([1,2,3,5], 5))


