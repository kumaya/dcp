# Snake and ladder


class QueueEntry(object):
    def __init__(self, v=0, d=0):
        self.v = v
        self.dist = d


def getMinDistance(N, move):
    # Keep track of visited nodes
    visited = [False] * N
    # Create queue for BFS
    bfs_q = []
    # Mark first node as visited
    visited[0] = True
    # Create an entry with node val and distance
    bfs_q.append(QueueEntry(0, 0))

    qe = QueueEntry()
    while bfs_q:
        qe = bfs_q.pop(0)
        # node num
        this_node = qe.v

        # We have traversed all nodes, return the distance now
        if this_node == N-1:
            break

        j = this_node + 1
        while j < N and j <= this_node+6:
            # ignore if already visited
            if not visited[j]:
                a = QueueEntry()

                # if not visited, calculate the move required to reach this cell
                # and mark this cell as visited
                a.dist = qe.dist + 1
                visited[j] = True

                # check if snake or ladder at 'j' and mark next node as their
                # end
                if move[j] != -1:
                    a.v = move[j]
                else:
                    a.v = j
                bfs_q.append(a)
            j += 1
    return qe.dist


if __name__ == '__main__':
    N = 100
    moves = [-1] * N

    # Ladders
    moves[1] = 38
    moves[4] = 14
    moves[9] = 31
    moves[21] = 42
    moves[28] = 84
    moves[36] = 44
    moves[51] = 67
    moves[71] = 91
    moves[80] = 100

    # Snakes
    moves[16] = 6
    moves[48] = 26
    moves[49] = 11
    moves[56] = 53
    moves[62] = 19
    moves[64] = 60
    moves[87] = 24
    moves[93] = 73
    moves[95] = 75
    moves[98] = 78

    print ("Minimum chance required to complete: %s" % getMinDistance(N, moves))