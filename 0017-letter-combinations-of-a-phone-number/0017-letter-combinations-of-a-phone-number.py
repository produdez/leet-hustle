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
        
        res = []
        def map_letters(i, prev=''):
            if i >= len(digits):
                res.append(prev)
                return 

            mappings = MAP[digits[i]]
            for char in mappings:
                map_letters(i+1, prev + char)
        
        if not digits: return []
        map_letters(0)
        return res