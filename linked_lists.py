class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_begining(self, data):
        # create a new node and let newest be the head
        newest = Node(data, self.head)
        self.head = newest
        self._size += 1

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def print(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
            print(llstr)


if __name__ == '__main__':
    # Driver function
    ll = linked_list()
    ll.insert_begining(2)
    ll.insert_begining(1)
    ll.insert_begining(99)
    ll.insert_end(6)
    ll.insert_end(9)
    ll.insert_end(3)
    ll.insert_end(4)
    ll.print()
