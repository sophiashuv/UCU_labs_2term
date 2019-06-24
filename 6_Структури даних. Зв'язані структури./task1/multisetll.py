from node import *        
import gc
# A class implementing Multiset as a linked list.


class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None
        self._size = 0

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest
        self._size += 1

    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next

            else:
                previous.next = current.next
            self._size -= 1

    def __len__(self):
        """
        The function that returns the size
        """
        return self._size

    def remove_all(self):
        """
        The function that removes for half
        """
        self._head = None
        gc.collect()

    def split_half(self):
        """
        The function that splits for half
        """
        if self._size <= 1:
            return None
        multiset1 = Multiset()
        multiset2 = Multiset()
        pr1, pr2 = self._head, self._head
        pr2_prev = self._head
        for i in range(self._size//2+1):
            pr2 = pr2.next
        for i in range(self._size//2):
            pr2_prev = pr2_prev.next
        pr2_prev.next = None
        multiset1._head = self._head
        multiset2._head = pr2
        return multiset1, multiset2

    def __str__(self):
        """
        The function returns the string presentation of multiset
        """
        node = self._head
        result = ""
        while node is not None:
            result += str(node.item) + " -> "
            node = node.next
        return result[:-3]


if __name__ == '__main__':
    data_set = Multiset()
    data_file = open("data.txt", "r")
    data_list = data_file.readlines()
    data_file.close()
    for line in data_list:
        data_set.add(line.strip())
    m, n = data_set.split_half()
    print(m)
    print(n)
    m.remove_all()
    print(m)
