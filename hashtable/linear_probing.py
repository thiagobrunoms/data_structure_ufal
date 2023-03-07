class Hashtable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        
    def __getitem__(self, key):
        index = self.hash(key)
        i = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            i += 1
            index = (self.hash(key) + i) % self.size
        raise KeyError(key)
        
    def __setitem__(self, key, value):
        index = self.hash(key)
        i = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            i += 1
            index = (self.hash(key) + i) % self.size
        self.keys[index] = key
        self.values[index] = value
        
    def hash(self, key):
        return hash(key) % self.size