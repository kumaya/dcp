# Given a linked list, rearrange the node values such that they appear in
# alternating low -> high -> low -> high ... form.


class Node(object):
    def __init__(self, v):
        self.data = v
        self.next = None


def high_low(head):
    if not head:
        return head
    low_case = True
    current = head
    while head and head.next:
        if low_case:
            if head.data > head.next.data:
                head.data, head.next.data = head.next.data, head.data
        else:
            if head.data < head.next.data:
                head.data, head.next.data = head.next.data, head.data
        low_case = not low_case
        head = head.next
    return current


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    new_head = high_low(head)
    print new_head.data,
    print new_head.next.data,
    print new_head.next.next.data,
    print new_head.next.next.next.data,
    print new_head.next.next.next.next.data
