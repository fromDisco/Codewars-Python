# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

# Timmy & Sarah think they are in love, but around where they live, 
# they will only know once they pick a flower each.
# If one of the flowers has an even number of petals and the other 
# has an odd number of petals it means they are in love.
 
# Write a function that will take the number of petals of each flower 
# and return true if they are in love and false if they aren't.


def lovefunc(flower1, flower2):
    # ^ is exclusive or, () are needed because of precedence
    love = (flower1 % 2 == 0) ^ (flower2 % 2 == 0) 

    return love 

print(lovefunc(1,4)) # True
print(lovefunc(2,2)) # False
print(lovefunc(0,1)) # True
print(lovefunc(0,0)) # False
