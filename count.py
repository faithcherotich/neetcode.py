# def Counter(strpram):
#     # intialize an empty dict
#     char_count={}
#     # loop through
#     for char in strpram:
#         # if the character is already in the dict, increment its count
#         if char in char_count:
#             char_count[char] += 1
#         # if the character is not in the dict, add it with a count of 1
#         else:
#             char_count[char] = 1
#             return char_count
# print(Counter("abcd"))


def Counter(s):
    char_count = {}
    # loop through each character
    for char in s:
        # if the char already exist increment
        if char in char_count:
            char_count[char] = 1
            # if not, add it with and count of 1
        else:
            char_count[char]= 1
            return char_count
print(Counter("abcd"))
            
    