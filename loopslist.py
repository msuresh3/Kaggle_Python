def count_negatives(nums):
    #return len([num for num in nums if num < 0])
    return sum([num < 0 for num in nums])

#print(count_negatives([5, -1, -2, 0, 3]))
#print (False + True + True + False + False)

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    #output = False
    #for num in nums:
    #    if num % 7 == 0:
    #        output = True
    #return output
    #return bool(sum([num%7 == 0 for num in nums]))
    return any([num % 7 == 0 for num in nums])

#print (has_lucky_number([2,3,4,5,6,7,8]))
#print (any([]))
#print (any([1]))
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [element > thresh for element in L]

#print (elementwise_greater_than([1, 2, 3, 4], 2))
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    prev = ""
    for menu in meals:
        if(prev == menu):
            print ('True')
        prev = menu
    return

print (menu_is_boring(['idly','dosa','chappathi','idly', 'idly', 'dosa', 'chappathi']))