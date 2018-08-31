# Given an array of integers, find the first missing positive integer
# in linear time and constant space. In other words, find the lowest
# positive integer that does not exist in the array. The array can contain
# duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2.
# The input [1, 2, 0] should give 3.


def find_missing(arr, lenArr):
    j = 0
    for i in range(0, lenArr):
        if arr[i] <= 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    for i in range(j, lenArr):
        if abs(arr[i])-1+j < lenArr:
            arr[abs(arr[i])-1+j] = -arr[abs(arr[i])-1+j]
    print arr
    for i in range(j, lenArr):
        if arr[i-1+j] > 0:
            return i-1+j
    return lenArr


if __name__ == "__main__":
    # l = [3, 4, -1, 1]
    # l = [1, 2, 0]
    l = [1, 2, 5, -7]
    lenArr = len(l)
    print find_missing(l, lenArr)
