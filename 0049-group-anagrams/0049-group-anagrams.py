class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Version 1
            Idea: 
                Encode all string to a dictionary count 
                and hash them in order to arrange into groups
            Complexity:
                Time: O(#num_str) * O(#num_char)
                Space: O(#num_str) [since could have unique encodings] * O(#avg_m) [average unique characters]
        '''
        groups = {}
        def encode(s):
            '''
                Time: O(n) build + O(n) convert to fset and hash
                Space: O(2m) dict + fset 
            '''
            dictionary = {}
            for char in s:
                dictionary[char] = dictionary.get(char, 0) + 1
            fset = frozenset(dictionary.items())
            return fset

        for s in strs:
            enc = encode(s)
            groups[enc] = groups.get(enc, []) + [s]
        return groups.values()