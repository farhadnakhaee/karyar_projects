# Write a code that takes two sorted lists as input and outputs a sorted listedlink

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def merge(self, head1, head2):
        if head1.value < head2.value:
            self.head = head1
            temp = head2
        else:
            self.head = head2
            temp = head1

        current = self.head

        while True:
            if current.next:
                if temp.value < current.next.value:
                    _next = current.next
                    current.next = temp
                    current = temp
                    temp = _next
                else:
                    current = current.next
            else:
                current.next = temp
                break
        return self.head


def create_linkedlist(lst):
    head = Element(lst.pop(0))
    temp = head
    while lst:
        temp.next = Element(lst.pop(0))
        temp = temp.next
    return head


lst1 = [1, 7, 5, 27, 28, 29]
lst2 = [2, 6, 9, 10, 11, 15, 16]

# create linkedlists
h1 = create_linkedlist(lst1)
h2 = create_linkedlist(lst2)

# merge two linkedlists
ll = LinkedList()
h = ll.merge(h1, h2)

# print final linkedlist
l = []
c = h
while c:
    l.append(c.value)
    c = c.next
print(l)
