# Given a binary tree convert it to full binary tree


class Node(object):
    def __init__(self, v):
        self.d = v
        self.l = None
        self.r = None


def convToFullBinaryTree(root):
    if not root:
        return root
    root.l = convToFullBinaryTree(root.l)
    root.r = convToFullBinaryTree(root.r)
    if not root.l and root.r:
        return root.r
    elif root.l and not root.r:
        return root.l
    else:
        return root

if __name__ == '__main__':
    root = Node(0)
    root.l = Node(1)
    root.l.l = Node(3)
    root.l.l.r = Node(5)
    root.r = Node(2)
    root.r.r = Node(4)
    root.r.r.l = Node(6)
    root.r.r.r = Node(7)

    convToFullBinaryTree(root)

    print root.d
    print root.l.d
    print root.r.d
    print root.r.l.d
    print root.r.r.d
