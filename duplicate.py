# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.



# def duplicate(nums):
#     # intitilize a set
#     seen = set()
#     # loop through each number in the list
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
    
# print(duplicate(input()))
    
def duplicateNumber(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
print(duplicateNumber(input()))
    