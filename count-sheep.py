# If you can't sleep, just count sheep!!
# Task:
# Given a non-negative integer, 3 for example,
# return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
# Input will always be valid, i.e. no negative integers.
def count_sheep(n):
    sheeps = ""
    for i in range(1, n + 1): 
        sheeps += str(i) + " sheep..."
    return sheeps

print(count_sheep(0))

# codewars solution
# https://www.codewars.com/kata/reviews/5b3fcb04fec6700205000299/groups/5b3fcb3f90576f0ad5000385
def count_sheep_codeWars(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))
