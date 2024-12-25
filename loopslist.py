def count_negatives(nums):
    #return len([num for num in nums if num < 0])
    return sum([num < 0 for num in nums])

print(count_negatives([5, -1, -2, 0, 3]))
print (False + True + True + False + False)
