# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# pseudocode


# define a function that takes a list as an argument
def same_first_last(numbers):
    # print the given list
    print("The given list is", numbers)
    # check if the first and last number of the list are the same
    if numbers[0] == numbers[-1]:
        # if they are the same return True
        return "the same. True."
    # if they are not the same return False
    else:
        return "not the same. False."


# write the given list
numbers_x = [10, 20, 30, 40, 10]
print("The first and last number of the list are", same_first_last(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("The first and last number of the list are", same_first_last(numbers_y))
