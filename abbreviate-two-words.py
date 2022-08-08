# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# 
# The output should be two capital letters with a dot separating them.
# 
# It should look like this:
def abbrev_name(name):
    splitName = name.title().split(" ")
    return splitName[0][0] + "." + splitName[1][0]

print(abbrev_name("Sam Harris"))

# codewars solution
# https://www.codewars.com/kata/reviews/5adf24ac82c8a1c88100176e/groups/5adf2b6560da5cc2bc00170b
def abbrevName_codeWars(name):
    return '.'.join(w[0] for w in name.split()).upper()
