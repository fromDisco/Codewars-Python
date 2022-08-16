# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# 
# The binary number returned should be a string.
# 
# Examples:(Input1, Input2 --> Output (explanation)))
def add_binary(a,b):
    sum = a + b
    binSum = ""
    
    while sum >= 1:
        if sum == 1:
            return str(sum) + binSum
        binSum = str(sum % 2) + binSum
        # IMPORTANT: with big numbers > n * 10**21 
        # simple division "a / b" results results in rounding errors
        # use "a // b" (floor Division)
        sum = sum // 2


print(add_binary(5695950263060609098732, 925125188997075983318))

# codewars solution
# https://www.codewars.com/kata/reviews/565f42510b9d78fa10000069/groups/566898a43e54f6e021000093
def add_binary(a, b):
    return format(a + b, 'b')
