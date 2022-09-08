# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.nn
def summation(num):
    return  sum(range(num + 1))
    
summation(8) # 36
