from math import inf

def max_crossing_subarray(array, low, mid, high):
    left_total = float(-inf)
    add_left = 0
    i = mid
    while(i >= 0):
        add_left = add_left + array[i]
        if(add_left > left_total):
            left_total = add_left
        i = i - 1
    right_total = float(-inf)
    add_right = 0
    j = mid + 1
    while(j <= high):
        add_right = add_right + array[j]
        if(add_right > right_total):
            right_total = add_right
        j = j + 1
    return left_total + right_total


def find_max_subarray(array, low, high):
    if(high == low):
        return array[low]
    else:
        mid = (low + high) // 2
        left_sum = find_max_subarray(array, low, mid)
        right_sum = find_max_subarray(array, mid + 1, high)
        cross_sum = max_crossing_subarray(array, low, mid, high)
        return max(left_sum, cross_sum, right_sum)
    

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = find_max_subarray(array, 0, len(array) - 1)
print(f"The maximum subarray sum is: {result}")


