# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# Time Complexity: O(n*logN)
def quickSort(arr, low, high):
    if low >= high:
        return
    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
    return arr


# Time Complexity: O(n)
def getSum(sortedL, lengthL, k):
    low = 0
    high = lengthL - 1
    while high > low:
        val = sortedL[high] + sortedL[low]
        if val == k:
            return True
        elif val > k:
            high -= 1
        else:
            low += 1
    return False


if __name__ == "__main__":
    inp = [10, 15, 3, 7]
    k = 17
    lengthL = len(inp)
    sortedL = quickSort(inp, 0, lengthL - 1)
    print(getSum(sortedL, lengthL, k))  # O(n*logN)
