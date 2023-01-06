class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        def encode(s):
            dictionary = {}
            for char in s:
                dictionary[char] = dictionary.get(char, 0) + 1
            fset = frozenset(dictionary.items())
            return hash(fset)

        for s in strs:
            enc = encode(s)
            groups[enc] = groups.get(enc, []) + [s]
        return list(groups.values())