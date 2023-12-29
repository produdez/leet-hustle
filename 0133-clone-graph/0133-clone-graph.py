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
        mapping = {}
        
        def dfs_clone(node):
            if node.val in mapping: return mapping[node.val] 
            
            copy = Node(node.val)
            mapping[node.val] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei)) # very smart solution (neetcode)
            
            return copy
        
        return dfs_clone(node)