class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = Node(head)

    def push(self, data: int):
        temp = Node(data)
        temp.data = data
        temp.next = self.head
        self.head = temp

    def iteractive_reverse(self):
        previous: Node = None
        current: Node = self.head
        next: Node = None

        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def show(self):
        currend = self.head
        while currend != None:
            print(currend.data)
            currend = currend.next


linkedList = LinkedList(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)
print('before reversing')
linkedList.show()
linkedList.iteractive_reverse()

print('after reversing')
linkedList.show()