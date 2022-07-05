class MyHashMap:

    def __init__(self):
        self.size = 2069 # use primary number
        self.mod_array = []
        for i in range(self.size):
            self.mod_array.append([])
            
        

    def put(self, key: int, value: int) -> None:
        mod = key%self.size
        self.remove(key)
        self.mod_array[mod].append((key, value))
        

    def get(self, key: int) -> int:
        mod = key%self.size
        for t in self.mod_array[mod]:
            if t[0] == key:
                return t[1]
            
        return -1
        
    def remove(self, key: int) -> None:
        mod = key%self.size
        #print(self.mod_array[mod])
        for t in self.mod_array[mod]:
            if t[0] == key:
                self.mod_array[mod].remove(t)
                break
                    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)