# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# 
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
def binary_array_to_number(arr):
    arr.reverse()
    num = 0

    for i, digit in enumerate(arr):
        if digit != 0:
            num = num + 2 ** i

    return num

print(binary_array_to_number([0,1,0,0]))
print(binary_array_to_number([1,1,1,1]))

# https://www.codewars.com/kata/reviews/578670e7d9456ea80500005e/groups/578670e7802dad02bf000331
def binary_array_to_number_codeWars(arr):
    return int("".join(map(str, arr)), 2)

print(binary_array_to_number([0,1,0,0]))
