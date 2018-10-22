# Invert a binary tree.


class Node():
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def invert(root):
    if not root:
        return
    else:
        left = invert(root.left)
        right = invert(root.right)
        root.left, root.right = right, left
    return root


if __name__ == '__main__':
    root = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f')))
    newT = invert(root)
    print newT.val, newT.left.val, newT.left.right.val, newT.right.val, newT.right.left.val
