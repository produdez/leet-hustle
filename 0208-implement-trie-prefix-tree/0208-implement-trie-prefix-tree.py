class Node:
    def __init__(self, char):
        self.children = {}
        self.char = char # Note: this is only for easy printing
        self.end = False
    def isRoot(self):
        return self.char == None
    def isWord(self):
        return self.end
    def print(self,level = 0):
        prefix = '    ' * level
        print(f'{prefix}char: {self.char}, end: {self.end}')
        for c in self.children:
            self.children[c].print(level+1)
class Trie:
    def __init__(self):
        self.root = Node(None)

    def print(self): 
        print('-----')
        self.root.print()
        print('-----')
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            
            node = node.children[c]
        
        node.end = True

    
    def _searchPrefix(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return (node, False)
            node = node.children[c]
        return (node, True)
    
    def search(self, word: str) -> bool:
        node, contains = self._searchPrefix(word)
        return contains and node.isWord()

    def startsWith(self, prefix: str) -> bool:
        _, contains = self._searchPrefix(prefix)
        return contains
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)