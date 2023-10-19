class Element(object):
    def __init__(self, lst: list):
        self.next = None
        self.value = None
        if lst:
            self.value = lst.pop(0)
            if lst:
                self.next = Element(lst)


class LinkedList(object):

    def merge_sorted(self, lst1, lst2):
        current1 = Element(lst1)
        current2 = Element(lst2)
        while current1 and current2:
            if current1.value and current2.value:
                if current1.value < current2.value:
                    yield current1.value
                    current1 = current1.next
                else:
                    yield current2.value
                    current2 = current2.next
            else:
                break

        while current1:
            if current1.value:
                yield current1.value
                current1 = current1.next
            else:
                break
        while current2:
            if current2.value:
                yield current2.value
                current2 = current2.next
            else:
                break
        

ll = LinkedList()
print(list(ll.merge_sorted([], [4, 5, 7, 9, 12])))
