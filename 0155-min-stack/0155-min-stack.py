'''
    Idea: keep a snapshot of min value at every node 
'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.minVal = min(next.minVal, val) if next else val
        self.next = next

class MinStack:
    
    def __init__(self):
        self.head = None
        self.length = 0
        

    def push(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self) -> None:
        temp = self.head
        self.head = self.head.next
        del temp
        self.length -= 1

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()