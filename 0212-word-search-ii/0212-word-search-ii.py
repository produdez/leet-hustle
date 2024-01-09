class Node:
    def __init__(self):
        self.end = False
        self.children = {}
        self.word = None
    def print(self, level=0):
        prefix = '  ' * level
        for char, children in self.children.items():
            print(f'{prefix}{char}{" - " + children.word if children.end else " ."}')
            children.print(level + 1)
class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.end = True
        node.word = word
    
    def remove(self, word):
        def delete(i, node):
            if node.end: node.end = False
            elif i >= len(word) or word[i] not in node.children:
                raise Error("Bruh what the fuck the word is not in dict?")
            else:
                char = word[i]
                if delete(i+1, node.children[char]):
                    node.children.pop(char)
            return len(node.children) == 0
        
        return delete(0, self.root)
            
            
    def print(self):
        self.root.print()
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dictionary = Trie()
        for word in words:
            dictionary.add(word)
        
        m, n = len(board[0]), len(board)
        result = set()
        visited = set()
        
        def dfs(i, j, node):
            if i not in range(n) or j not in range(m): return
            if (i,j) in visited: return
            
            char = board[i][j]
            if char not in node.children: return

            visited.add((i,j))

            nxt = node.children[char]
            if nxt.end: 
                result.add(nxt.word)
                dictionary.remove(nxt.word)

            dfs(i, j-1, nxt)
            dfs(i-1, j, nxt)
            dfs(i, j+1, nxt)
            dfs(i+1, j, nxt)            
            visited.remove((i,j))

        for i in range(n):
            for j in range(m):
                dfs(i,j, dictionary.root)
        
        return result