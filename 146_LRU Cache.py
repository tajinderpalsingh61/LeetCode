#### Solution 1: using OrderedDict

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.keys():
            self.move_to_end(key)
            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys():
            self.move_to_end(key)
            
        self[key] = value
            
        if len(self.keys()) > self.capacity:
            self.popitem(last=False)
            
        
      
        

#### Solution 1: using Double Linked List
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
        
class LRUCache():
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
    
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value
        
    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            node = DLinkedNode()
            node.key = key
            node.value = value
            self.cache[key] = node
            self._add_node(node)

            self.size+=1

            if self.size > self.capacity:
                last = self._pop_tail()
                del self.cache[last.key]
                self.size-=1

        else:
            node.value = value
            self._move_to_head(node)
