# Exercise 1: Write a function called chop that takes a list and modifies it, removing
# the first and last elements, and returns None. Then write a function called middle
# that takes a list and returns a new list that contains all but the first and last
# elements.


def chop(t):
    """Remove the first and last elements from a list in place and return None."""
    del t[0]
    del t[-1]
    return None


def middle(t):
    """Return a new list containing all elements except the first and last."""
    return t[1:-1]


# Example usage:
# numbers = [1, 2, 3, 4, 5]
# chop(numbers)
# print(numbers)  # [2, 3, 4]
# print(middle([1, 2, 3, 4, 5]))  # [2, 3, 4]
