class Node:
    def __init__(self,key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt
    def __str__(self):
        return f'({self.key}, {self.value}) -> {str(self.next) if self.next else ""}'

class LRUCache:
    '''
        Version: 1.5
            Stop using dummy head/tail
        Idea:
            1. HashMap for key -> node
                HashMap hold the whole node so as to have
                reference to the link list and re-order it
            2. Doubly Link List for ordering
                -> Why double? cause we need to keep track of 
                both oldest and add newest
            3. This version use dummy node for head and tail of
                the doubly linked list
            4. There's a handy log function wrapper to log things
        Complexity:
        - Time: get & set O(1)
        - Space: get & set O(1)
        - Total space: O(2n) for n being #key in cache
            
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = self.right = None
        self.cache = {}
    
    def log(func):
        def wrap(self,*args):
            print(f'---{func.__name__}{args}---')
            result = func(self,*args)
            print(f'size: {len(self.cache)}, cap: {self.capacity}')
            print('queue: ', str(self.left))
            return result
        return wrap
    
    def _append(self, node):
        if not self.left: 
            self.left = self.right = node
        else:
            node.prev = self.right
            node.next = None
            self.right.next = node
            self.right = node
    def _remove(self, node):
        if node == self.left: self.left = node.next
        if node == self.right: self.right = node.prev
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next
        
    # @log
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove(node)
        self._append(node)
        return node.value

    # @log
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache: # override value and stich neighbors
            self.cache[key].value = value
            node = self.cache[key]
            self._remove(node)
        else: # create and write cache
            node = Node(key, value)
            self.cache[key] = node
        
        # update order relative to the end
        self._append(node)
        
        # correction if over cap
        if len(self.cache) > self.capacity:
            self.cache.pop(self.left.key)
            self._remove(self.left)
                        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)