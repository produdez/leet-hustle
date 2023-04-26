class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAP = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        def map_letters(i, prev=''):
            if i == len(digits):
                res.append(prev)
                return 

            for char in MAP[digits[i]]:
                map_letters(i+1, prev + char)
        
        if not digits: return []
        map_letters(0)
        return res