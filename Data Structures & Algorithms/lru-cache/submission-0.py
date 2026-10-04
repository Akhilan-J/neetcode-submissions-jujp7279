class Node:
    def __init__(self,value,key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.front = Node(0,0) # least recently used
        self.back = Node(0,0) # most recently used
        self.cache = {}
        self.capacity = capacity
        self.front.next = self.back
        self.back.prev = self.front

    def _insert(self,node):
        temp = self.back.prev
        temp.next = node
        node.prev = temp
        node.next = self.back
        self.back.prev = node
    
    def _del(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._del(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                #evict
                evict = self.front.next
                self._del(evict)
                node = Node(value,key)
                self._insert(node)
                del self.cache[evict.key]
                self.cache[key] = node
                return
            else:
                node = Node(value,key)
                self._insert(node)
                self.cache[key] = node
                return
        else:
            #update
            node = self.cache[key]
            node.value = value
            self._del(node)
            self._insert(node)
            return 

        
