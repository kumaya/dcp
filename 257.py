# Given an array of integers out of order, determine the bounds of the
# smallest window that must be sorted in order for the entire array
# to be sorted


def smallest_window(inp):
    l_inp = len(inp)
    # candidate subarray
    s = 0
    h = 0
    for i in range(l_inp-1):
        if inp[i+1] < inp[i]:
            s = i
            break
    for j in range(l_inp-1, 0, -1):
        if inp[j] < inp[j-1]:
            h = j
            break
    minE = min(inp[s:h+1])
    maxE = max(inp[s:h+1])
    if s == 0 and h == 0:
        return -1

    k, l = 0, 0
    for i in range(0, s):
        if inp[i] > minE:
            k = i
            break
        else:
            k = s

    for j in range(l_inp-1, h-1, -1):
        if inp[j] < maxE:
            l = j
            break
        else:
            l = h
    return k, l


if __name__ == '__main__':
    # inp = [3, 7, 5, 6, 9]
    # inp = [3, 10, 5, 12, 9]
    inp = [3, 10, 5, 12, 13]
    # inp = [1,2,3,4,5,6]
    print smallest_window(inp)
