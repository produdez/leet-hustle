class Node:
    def __init__(self,key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt
    def __str__(self):
        return f'({self.key}, {self.value}) -> {str(self.next) if self.next else ""}'
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        
        self.left = Node(None, -1)
        self.right = Node(None, -1)
        self.right.prev=self.left
        self.left.next = self.right
        
        self.cache = {}
    
    def log(func):
        def wrap(self,*args):
            print(f'---{func.__name__}{args}---')
            result = func(self,*args)
            print(f'size: {self.size}, cap: {self.capacity}')
            # temp = self.left
            # out = ''
            # while temp:
            #     out += str(temp.value) + '->'
            #     temp = temp.next
            # print(out)
            # print(f'-result: {result}-')
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
        
        if key in self.cache: # override
            self.cache[key].value = value
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else: # create and write cache
            node = Node(key, value)
            self.cache[key] = node
            self.size += 1
        
        # update order
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next = node
        self.right.prev = node
        
        # correction if over cap
        if self.size > self.capacity:
            self.size -= 1
            self.cache.pop(self.left.next.key)
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
                        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)