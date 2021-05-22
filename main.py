# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
from statistics import mean
def average(num_list):
    avg = mean(num_list)
    print ("the average is", avg )
    return avg

average([1,2,3])
