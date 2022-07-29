def count_by(x, n):
    """
    Create a function with two arguments that will return an array of the first (n) multiples of (x).

    Assume both the given number and the number of times to count will be positive numbers greater than 0.

    Return the results as an array (or list in Python, Haskell or Elixir).
    """
    count = 0
    numList = []
    
    while count < n:
        count += 1
        numList.append(x * count)

    return numList


print(count_by(1, 5)) # [1, 2, 3, 4, 5]
print(count_by(2, 5)) # [2, 4, 6, 8, 10]


# codewars solutions
def count_by_CW1(x, n):
    """
    https://www.codewars.com/kata/reviews/551609a119aab6c5240000b5/groups/551609a119aab6c5240000b7
    """
    return range(x, x * n + 1, x)


def count_by_CW2(x, n):
    """
    https://www.codewars.com/kata/reviews/551609a119aab6c5240000b5/groups/5517089a236c8825230002e8
    """
    return [i * x for i in range(1, n + 1)] #