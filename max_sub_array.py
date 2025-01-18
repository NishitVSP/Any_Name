from math import inf # importing inf to assign variables with -infinity.

"""
This code will be solving maximum subarray problem by using a divide and conquer algorithm.
"""
def max_crossing_subarray(array, low, mid, high):
    """
    max_crossing_subarray is a function which will return maximum sum
    which can be achieved by picking elements from left sub-array as well as right sub-array.

    Args: array(which is a list containing integers) and three pointers low, mid & high.

    Returns: an integer which is the sum of the maximum total sum in the left sub-array & 
             maximum total sum in the right sub-array.
    """
    left_total = -inf  # initializing left_total with -infinity.
    add_left = 0
    max_left = mid  # initial assumption for left boundary
    for i in range(mid, low - 1, -1):  # loop to traverse the left sub-array and find the max sum
        add_left += array[i]
        if add_left > left_total:
            left_total = add_left
            max_left = i
    right_total = -inf  # initializing right_total with -infinity.
    add_right = 0
    max_right = mid + 1  # initial assumption for right boundary
    for j in range(mid + 1, high + 1):  # loop to traverse the right sub-array and find the max sum
        add_right += array[j]
        if add_right > right_total:
            right_total = add_right
            max_right = j
    return left_total + right_total, max_left, max_right


def find_max_subarray(array, low, high):
    """
    find_max_subarray is the function which will divide the array recursively 
    and find the maximum sub-array.

    Args: a array (which is a list of integers) and two integer values low & high 
          to calculate mid.

    Base Case: if high == low i.e., we have reached an array of length 1, 
               containing only a single element. This single element is 
               the only possible total maximum sum, so return that same element.

    Returns: the total sum of the maximum sub-array, two pointers to retrieve the max sub-array.
    """
    if high == low:  # base case
        return array[low], low, high
    mid = (low + high) // 2  # dividing the array into two halves
    # Recursively find the maximum subarray in the left and right subarrays
    left_sum, left_sub_max_left, left_sub_max_right = find_max_subarray(array, low, mid)
    right_sum, right_sub_max_left, right_sub_max_right = find_max_subarray(array, mid + 1, high)
    # To find the max sum of elements crossing the left and right subarrays
    cross_sum, cross_max_left, cross_max_right = max_crossing_subarray(array, low, mid, high)
    # Determine which subarray has the maximum sum
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_sub_max_left, left_sub_max_right
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_sub_max_left, right_sub_max_right
    else:
        return cross_sum, cross_max_left, cross_max_right


# Test the implementation
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result, start, end = find_max_subarray(arr, 0, len(arr) - 1)
print(f"The maximum subarray sum is: {result}")
print("The maximum sub-array is:")
print(arr[start:end + 1])
