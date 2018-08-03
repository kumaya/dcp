# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node, s, w, k):
    if not node:
        return s
    else:
        left = serialize(node.left, s, 'l', k+1)
        s += str(k) + w + "." + node.val + ","
        right = serialize(node.right, s, 'r', k+1)
        return left + right


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    s = ""
    se = serialize(node, s, '', k=0)
    print se