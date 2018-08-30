# Compute the running median of a sequence of numbers.
# That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
from heapq import heappush, heappop


def median(inp):
    minHeap, maxHeap = [], []
    for i in inp:
        if len(maxHeap) > len(minHeap):
            if i < maxHeap[0]:
                heappush(minHeap, -i)
            else:
                heappush(minHeap, -heappop(maxHeap))
                heappush(maxHeap, i)
        elif len(minHeap) > len(maxHeap):
            if i >= -minHeap[0]:
                heappush(maxHeap, i)
            else:
                heappush(maxHeap, -heappop(minHeap))
                heappush(minHeap, -i)
        else:
            if not maxHeap:
                heappush(maxHeap, i)
            elif i < maxHeap[0]:
                heappush(minHeap, -i)
            else:
                heappush(maxHeap, i)
        if len(maxHeap) > len(minHeap):
            print("%d" % float(maxHeap[0]))
        elif len(minHeap) > len(maxHeap):
            print("%.1f" % float(-minHeap[0]))
        else:
            print("%.1f" % float(((maxHeap[0])+(-minHeap[0]))/2.0))


if __name__ == "__main__":
    inp = [2, 1, 5, 7, 2, 0, 5]
    median(inp)
