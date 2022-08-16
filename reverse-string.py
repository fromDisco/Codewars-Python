# Complete the solution so that it reverses the string passed into it. 
def solution(string):
    strArr = list(string)
    strArr.reverse()
    return "".join(strArr) 

print(solution('world'))

# codewars solution
# https://www.codewars.com/kata/reviews/54e10e357775b79e2800011c/groups/54e10e367775b79e2800011e
def solution_codeWars(str):
  return str[::-1]

print(solution_codeWars('world'))
