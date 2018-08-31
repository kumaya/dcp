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


def rev_inorder(node, v=[0]):
    if not node or v[0] >= 2:
        return
    else:
        rev_inorder(node.right, v)
        v[0] += 1
        if v[0] == 2:
            print node.val
            return
        rev_inorder(node.left, v)


def search(node):
    return inorder(node, [])[-2]


def search_iter(node):
    second = None
    root = node
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
        if node == root:
            second = node.val
    return second


if __name__ == "__main__":
    node = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    print "Second largest node with space:", search(node)
    print "Second largest node iteratively:", search_iter(node)
    print "second largest node using recursion:",
    rev_inorder(node)