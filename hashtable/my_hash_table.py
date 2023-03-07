from linked_list import *


class MyHashTable:
    def __init__(self):
        self.capacity = 30
        self.items: LinkedList = [None] * self.capacity
        self.size = 0

    def __calculate_bucket(self, item):
        item_hash = hash(item)
        bucket = item_hash % len(self.items)
        return bucket

    def put(self, key: int, value):
        self.__ensure_capacity()

        bucket = self.__calculate_bucket(key)
        item: ListNode = ListNode(key, value)
        if self.items[bucket] != None:
            bucket_list: LinkedList = self.items[bucket]
            bucket_list.insert(item)
        else:
            bucket_list = LinkedList(item)
            self.items[bucket] = bucket_list

        self.size += 1

    def __ensure_capacity(self):
        if self.size == self.size * 0.7:
            self.capacity += 10
            temp = [None] * self.capacity
            for items in self.items:
                temp.append(items)

            self.items = temp

    def delete(self, key) -> bool:
        bucket = self.__calculate_bucket(key)
        bucket_list: LinkedList = self.items[bucket]
        if bucket_list == None:
            return False

        key_t = (key,)
        result = bucket_list.delete_by_key(key_t)
        if result:
            self.size -= 1

    def getItem(self, key):
        bucket = self.__calculate_bucket(key)
        
        print('self.items[bucket]', self.items[bucket])
        if self.items[bucket] == None: return None

        linkedList: LinkedList = self.items[bucket]

        return linkedList.getItem(key)

    def show(self):
        print(self.items)
        for item in self.items:
            if item != None:
                print(item.show())


s = MyHashTable()
for i in range(25):
    s.put(i, i * 100)
# s.show()

# s.delete(17)
# s.show()
element_found = s.getItem(20)
if (element_found != None):
    print(element_found.id)
    print(element_found.value)
else:
    print('Item não encontrado!')