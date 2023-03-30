class Element:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.rmv_eligible = False

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.items: Element = [None] * size
        
    def __getitem__(self, key):
        index = self.calculate_bucket(key)
        i = 0
        while self.items[index] is not None:
            if self.items[index].id == key:
                return self.items[index]
            i += 1
            index = (self.hash(key) + i) % self.size #use i ** 2 for quadratic probin
        raise KeyError(key)
        
    def __setitem__(self, key, value):
        index = self.calculate_bucket(key)
        i = 0
        while self.items[index] is not None:
            if self.items[index].id == key:
                self.items[index] = value
                return
            
            i += 1
            index = (self.hash(key) + i) % self.size #use i ** 2 for quadratic probin

        self.items[index] = value

    def __remove__(self, key):
        index = self.calculate_bucket(key)
        i = 0
        while self.items[index] is not None:
            if self.items[index].id == key:
                self.items[index].rmv_eligible = True
                return

            i += 1
            index = (self.calculate_bucket(key) + i) % self.size #use i ** 2 for quadratic probin

        
    def calculate_bucket(self, key):
        return hash(key) % self.size