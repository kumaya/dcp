# Given the root to a binary search tree, find the second largest node in the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(node, v=[]):
    if not node:
        return None
    else:
        inorder(node.left, v)
        v.append(node.val)
        inorder(node.right, v)
    return v


def search(node):
    return inorder(node, [])[-2]


def search_iter(node):
    second = None
    if not node:
        return
    while node.right:
        second = node.val
        node = node.right
    if node.left:
        node = node.left
        while node.right:
            node = node.right
        second = node.val
    else:
        second = node.val
    return second


if __name__ == "__main__":
    node = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    print "Second largest node:", search(node)
    print "Second largest node iteratively:", search_iter(node)