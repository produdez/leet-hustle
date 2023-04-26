class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAP = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        
        def map_letters(i):
            if i >= len(digits): return
            
            mappings = MAP[digits[i]]
            for _ in range(len(res)):
                prev = res.popleft()
                for mapping in mappings:
                    res.append(prev + mapping)
                  
            map_letters(i+1)
        
        if not digits: return []
        res = collections.deque(MAP[digits[0]])
        map_letters(1)
        return res