# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?
def make_negative(number):
    if number < 0: 
        return number
    else:
        return number * -1

print(make_negative(4))

# codewars solution
# https://www.codewars.com/kata/reviews/556a410ed44ca75d15000023/groups/556a7c127f9171f02d0000e9
def make_negative_codeWars( number ):
    return -abs(number)

