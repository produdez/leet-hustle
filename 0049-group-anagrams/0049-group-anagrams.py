class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Version 2
                Update with array encode
            Idea: 
                Encode all string to a dictionary count 
                and hash them in order to arrange into groups
            Complexity:
                Time: O(#num_str) * O(#num_char)
                Space: O(#num_str) [since could have unique encodings] * O(#avg_m) [average unique characters]
        '''
        groups = defaultdict(list)
        def encode(s):
            '''
                Time: O(n)
                Space: O(1) 
            '''
            count = [0] * 26
            for char in s:
                count[ord(char) - 97] += 1
            return hash(tuple(count))

        for s in strs:
            groups[encode(s)].append(s)
        return groups.values()