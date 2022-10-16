# Destructive vs Non-Destructive functions


# A non-destructive function takes in a list and returns a new list
def double_non_destructive(nums):

    new_list = []

    for num in nums:
        new_list.append(num*2)
    
    return new_list


# A destructive function takes in a list and changes it directly
def double_destructive(nums):
    for i in range(len(nums)):
        nums[i] *= 2

    # We do not need to return, as changes to the list have already been made


numbers = [1, 4, 7, 2]

# Note that we store the result here, since the function returns a new list
double_numbers = double_non_destructive(numbers)
print(double_numbers)

# Note that we do not store the result here, since we do not return in the function
double_destructive(numbers)
print(numbers)
