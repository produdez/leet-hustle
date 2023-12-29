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
        res = {node.val: Node(node.val)}
        queue = [node]
        while queue:
            cur = queue.pop()                
            copy = res[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in res:
                    res[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                copy.neighbors.append(res[neighbor.val])
                
                    
        return res[node.val]
            