def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    #keep track of 3 values to do a binary search
    bottom = 0
    top = len(arr) - 1
    mid = int((top + bottom) / 2)

    #edge case: empty array, return -1
    if len(arr) == 0:
        return -1

    #search middle value between top and bottom each search, then cut search area in half and repeat
    while top - bottom > 1:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            bottom = mid
            mid = int((top + bottom) / 2)
        elif arr[mid] > target:
            top = mid
            mid = int((top + bottom) / 2)

    #check the last two remaining values, then return -1 if not in the array
    if arr[top] == target:
        return top
    elif arr[bottom] == target:
        return bottom
    else:
        return -1


    return -1  # not found
