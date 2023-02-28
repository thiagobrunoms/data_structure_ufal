class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoubledLinkedList:
    def __init__(self):
        self.head = None

    #Adiciona no início
    def push(self, node: Node):
        if (self.head == None):
            self.head = node
            return
        
        node.next = self.head
        self.head.previous = node
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
            if self.head.next != None:
                self.head = self.head.next
                self.head.previous = None
            else:
                self.head = None

            return temp

        position = 1
        previous = self.head
        current = self.head.next
        while (position < index):
            previous = current
            current = current.next
            position = position + 1
        
        if (current.next != None):
            previous.next = current.next
            current.next.previous = current.previous
        else:
            previous.next = None

        return current

    def show(self):
        current = self.head
        while(current != None):
            print('================================')
            print('valor do current', current.value)
            if (current.previous != None):
                print('valor do previous', current.previous.value)
            
            if (current.next != None):
                print('valor do next', current.next.value)


            current = current.next


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
minha_lista = DoubledLinkedList()
minha_lista.push(node0)
minha_lista.push(node1)
minha_lista.push(node2)
minha_lista.push(node3)
minha_lista.show()
print('== Removendo primeiro elemento!')
node_removido = minha_lista.remove(3)
print('== Node removido', node_removido.value)

print('\n\n\nNova lista')
minha_lista.show()
# # minha_lista.push(node1)
# # minha_lista.push(node2)
# # minha_lista.push(node3)
# # minha_lista.show()
