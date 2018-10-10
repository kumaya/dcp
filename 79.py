# Given an array of integers, write a function to determine whether the array
# could become non-decreasing by modifying at most 1 element.
#
# For example, given the array [10, 5, 7], you should return true, since
# we can modify the 10 into a 1 to make the array non-decreasing.
#
# Given the array [10, 5, 1], you should return false, since we can't
# modify any one element to get a non-decreasing array.


def nonDecreasingArr(arr, larr, k):
    count = 0
    for i in range(larr-1):
        if arr[i] > arr[i+1] and count >= k:
            return False
        elif arr[i] > arr[i+1]:
            count += 1
    return True


if __name__ == "__main__":
    arr = [10, 5, 7]
    larr = len(arr)
    k = 1
    print nonDecreasingArr(arr, larr, k)
