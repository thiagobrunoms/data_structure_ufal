class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #REPRESENTA UM NODE

class LinkedList:
    def __init__(self):
        self.head = None

    #Adiciona no início
    def push(self, node: Node):
        if (self.head == None):
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    #Adiciona no fim
    def add(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while (temp.next != None):
            temp = temp.next

        temp.next = new_node

    #Remove e retorna o nó removido
    def remove(self, index: int):
        if (index == 0):
            temp = self.head
            self.head = self.head.next
            return temp

        position = 1
        previous = self.head
        current = self.head.next
        while (position < index):
            previous = current
            current = current.next
            position = position + 1
        
        previous.next = current.next
        return current

    def show(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
minha_lista = LinkedList()
minha_lista.add(node1)
minha_lista.add(node2)
minha_lista.add(node3)
minha_lista.show()
print('Removendo primeiro elemento!')
node_removido = minha_lista.remove(0)
print('Node removido', node_removido.value)

print('Nova lista')
minha_lista.show()
# minha_lista.push(node1)
# minha_lista.push(node2)
# minha_lista.push(node3)
# minha_lista.show()
