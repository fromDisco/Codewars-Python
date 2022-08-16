# Complete the solution so that the function will break up camel casing,
# using a space between words.
def solution(s):
    index = []
    for i, letter in enumerate(s):
        print(i)
        # if 65 >= ord(letter) <= 90:
        #     index.append(i)


print(solution(solution("AaaZBabbZ")))
