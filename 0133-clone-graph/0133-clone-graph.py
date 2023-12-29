"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return 
        res = {}
        queue = collections.deque([node])
        done = set([1])
        while queue:
            cur = queue.popleft()
            if cur.val not in res: res[cur.val] = Node(cur.val)
                
            copy = res[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in res:
                    res[neighbor.val] = Node(neighbor.val)
                copy.neighbors.append(res[neighbor.val])
                
                if neighbor.val not in done: 
                    queue.append(neighbor)
                    done.add(neighbor.val)
                    
        return res[node.val]
            