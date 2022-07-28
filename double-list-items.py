# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]
def maps(list):
    double = []

    for item in list:
        double.append(item * 2)

    return double
    
print(maps([1, 2, 3]))

# https://www.codewars.com/kata/reviews/57fbf74b777d18094c0000e4/groups/57fc882f3206fb65be000b88
def mapsCodeWars(list):
    return [2 * x for x in list]

print(mapsCodeWars([3, 4, 5]))
