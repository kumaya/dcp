# Given the head of a singly linked list, reverse it in-place.


class Node:
    def __init__(self, data, next=None):
        self.node = next
        self.data = data


def printList(head):
    while head:
        print head.data, "->",
        head = head.node
    print ""


def reverseList(head):
    prev = nextP = None
    while head:
        nextP = head.node
        head.node = prev
        prev = head
        head = nextP
    printList(prev)

if __name__ == "__main__":
    ll = Node(1, Node(2, Node(3)))
    printList(ll)
    reverseList(ll)