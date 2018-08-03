# Given a list of integers, write a function that returns the largest sum
# of non-adjacent numbers. Numbers can be 0 or negative.

# For example,
# [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.


def get_sum(arr):
    if arr[1] < arr[0]:
        arr[1] = arr[0]
    for i in range(2, len(arr)):
        arr[i] = max(arr[i], arr[i - 2] + arr[i])
        arr[i] = max(arr[i], arr[i - 1])
    return arr[-1]


if __name__ == "__main__":
    l = [2, 4, 6, 2, 5]
    print get_sum(l)
