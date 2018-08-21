# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node, l):
    if not node:
        l.append(-1)
    else:
        l.append(node.val)
        serialize(node.left, l)
        serialize(node.right, l)
    return " ".join(str(x) for x in l)


def deserialize(s):
    serializedLst = s.split(" ")
    if len(serializedLst) == 0:
        return Node(None)
    return formTree(serializedLst)


def formTree(serializedLst):
    if len(serializedLst) > 0:
        val = serializedLst.pop(0)
        if val != '-1':
            node = Node(val)
            node.left = formTree(serializedLst)
            node.right = formTree(serializedLst)
        else:
            node = Node(None)
    return node


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print serialize(node, [])
    serializedString = serialize(node, [])
    assert deserialize(serializedString).left.left.val == 'left.left'