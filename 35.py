# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values
# of the array so that all the Rs come first, the Gs come second, and the Bs come last.
# You can only swap elements of the array.

def swap(inp, len_inp):
    pR = 0
    pB = len_inp - 1
    temp = 0
    while pR <= pB:
        if inp[temp] == "R":
            inp[temp], inp[pR] = inp[pR], inp[temp]
            pR += 1
            temp += 1
        elif inp[temp] == "B":
            temp += 1
        else:
            inp[temp], inp[pB] = inp[pB], inp[temp]
            pB -= 1
    return inp

if __name__ == "__main__":
    inp = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    print "Input:", inp
    print "Output:", swap(inp, len(inp))