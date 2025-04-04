class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            index += 1
            index = index % self.capacity

        return None
    
    def put(self, key, value):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size == self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].key = value
                return
            index += 1
            index = index%self.capacity

    def rehash(self):
        oldMap = self.map
        self.capacity *= 2
        newMap = [None]*self.capacity
        self.map = newMap
        self.size = 0

        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.value)
    
    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return 
            index += 1
            index %= self.capacity
    
    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.value)


#Examples 

hashMap = HashMap()

#Adding items to our hash table
hashMap.put("alex", 21)
hashMap.put("merry", 17)
hashMap.put("chuck", 35)
hashMap.put("john", 28)
hashMap.put("sarah", 25)
hashMap.put("jessy", 24)

hashMap.print()

# removing
hashMap.remove("chuck")
hashMap.remove("sarah")

print("____________________________")
hashMap.print()
