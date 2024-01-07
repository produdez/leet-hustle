class TrieNode:
    def __init__(self, char = None):
        self.char = char
        self.end = False
        self.neighbors = {}
class WordDictionary:
    def __init__(self):
        self.dictionary = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.dictionary
        for char in word:
            if char not in node.neighbors:
                node.neighbors[char] = TrieNode(char)
            
            node = node.neighbors[char]
        
        node.end = True
    
    def _search(self, start, word):
        node = start
        for idx, char in enumerate(word):
            if char is '.':
                for neighbor in node.neighbors.values():
                    if self._search(neighbor, word[idx+1:]): 
                        return True
            if char not in node.neighbors:
                return False
            
            node = node.neighbors[char]
        
        return node.end
    def search(self, word: str) -> bool:
        return self._search(self.dictionary, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)