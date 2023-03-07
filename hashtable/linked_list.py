class ListNode:
    def __init__(self, key: int, value, next=None):
        self.id = key
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head
        self.size = 0

    def insert(self, node: ListNode):
        if (self.head == None):
            self.head = node
            self.size += 1
            return

        node.next = self.head
        self.head = node
        self.size += 1

    def insertAt(self, index: int, node: ListNode) -> bool:
        if index == 0:
            self.insert(node)
            self.size += 1
            return True

        current = self.head
        previous = None

        count = 1
        while current != None:
            if count == index:
                node.next = current
                previous.next = node
                self.size += 1
                return True

            previous = current
            current = current.next
            count += 1

        return False

    def delete(self, position: int) -> bool:
        if position > self.size or position < 0:
            return False

        if position == 0:
            self.head = self.head.next

        current = self.head
        previous = None
        count = 1
        while count < self.size:
            if position == count:
                previous.next = current.next

            previous = current
            current = current.next
            count += 1

    def delete_by_key(self, key: tuple) -> bool:
        if self.head.id == key:
            self.head = self.head.next
            return True

        current = self.head
        privious = None
        while current != None:
            if current.id == key:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False
    
    def getItem(self, key):
        if (self.head != None and self.head.id == key):
            return self.head
        
        current = self.head.next
        while (current != None):
            if (current.id == key): return current
            current = current.next

        return None

    def show(self):
        current = self.head
        while (current != None):
            print('key', current.id, 'value', current.value)
            current = current.next


# n1 = Node(1, 10)
# n2 = Node(2, 20)
# n3 = Node(3, 30)
# n4 = Node(4, 40)
# n5 = Node(5, 25)

# linkedList = LinkedList(n1)
# linkedList.insert(n2)
# linkedList.insert(n3)
# linkedList.insert(n4)
# linkedList.show()
# print('=====')
# linkedList.insertAt(2, n5)
# linkedList.show()
# print('=====')
# linkedList.delete(2)
# linkedList.show()