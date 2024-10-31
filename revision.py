def duplicate(nums):
    # initialize an empty dict
    num_count={}
    # loop through the dict
    for num in nums:
        # check if its alredy exist
        if num in num_count:
            return True  
        
        # if not, add it with a count of 1
        num_count[num]=1
#     return False
# print(duplicate(input()))    


def isAnagram(s, t):
    return sorted(s)==sorted(t)
print(isAnagram("listen","silent"))