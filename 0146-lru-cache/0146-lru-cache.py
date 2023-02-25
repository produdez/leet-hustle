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
        Version: 1
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
        self.left = Node(None, -1)
        self.right = Node(None, -1)
        self.right.prev=self.left
        self.left.next = self.right
        self.cache = {}
    
    def log(func):
        def wrap(self,*args):
            print(f'---{func.__name__}{args}---')
            result = func(self,*args)
            print(f'size: {len(self.cache)}, cap: {self.capacity}')
            print('queue: ', str(self.left))
            return result
        return wrap
    
    # @log
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        # stich
        node.prev.next = node.next
        node.next.prev = node.prev
        # update order
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next = node
        self.right.prev = node
        
        return node.value

    # @log
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache: # override value and stich neighbors
            self.cache[key].value = value
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else: # create and write cache
            node = Node(key, value)
            self.cache[key] = node
        
        # update order relative to the end
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next = node
        self.right.prev = node
        
        # correction if over cap
        if len(self.cache) > self.capacity:
            self.cache.pop(self.left.next.key)
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
                        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)