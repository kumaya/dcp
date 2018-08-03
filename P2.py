# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.


def product(inp):
    total = 1
    for i in inp:
        total *= i
    out = []
    for i in inp:
        out.append(total/i)
    return out


def productWithoutDivision(inp):
    len_inp = len(inp)
    l_arr = [0] * len_inp
    l_arr[0] = 1
    for i in range(1, len_inp):
        l_arr[i] = l_arr[i-1] * inp[i-1]
    r_arr = [0] * len_inp
    r_arr[-1] = 1
    for i in range(len_inp-2, -1, -1):
        r_arr[i] = r_arr[i+1] * inp[i+1]
    out = []
    for i, j in zip(l_arr, r_arr):
        out.append(i*j)
    return out

if __name__ == "__main__":
    inp = [1, 2, 3, 4, 5]
    print "With division:", product(inp)
    print "Without division:", productWithoutDivision(inp)
