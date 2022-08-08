# Given a list of integers, determine whether the sum of its elements is odd or even.
# 
# Give your answer as a string matching "odd" or "even".
# 
# If the input array is empty consider it as: [0] (array with a zero).
def odd_or_even(arr):
    sum = 0
    for num in arr:
        sum += num

    return "even" if sum % 2 == 0 else "odd"

print(odd_or_even([0, 1, 2]))
