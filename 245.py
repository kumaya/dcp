"""You are given an array of integers, where each element represents the
maximum number of steps that can be jumped going forward from that element.
Write a function to return the minimum number of jumps you must take in
order to get from the start to the end of the array.
For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2,
 as the optimal solution involves jumping from 6 to 5, and then from 5 to 9."""


def minJumps(a):
    i, index, count = 0, 0, 0
    while i <= len(a):
        high = 0
        for j in range(i, a[i]+1+i):
            tmp = j + a[j]
            if high < tmp:
                high = tmp
                index = j
        print "===", index,
        if index == 0:
            return -1
        i += index
        count += 1
    return count


if __name__ == '__main__':
    a = [6,0,0,0,0,0,0,0,4]
    print("jump=%d" % minJumps(a))
    b = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print("jump=%d" % minJumps(b))
    c = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
    print("jump=%d" % minJumps(c))
    d = [0, 6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
    print("jump=%d" % minJumps(d))
