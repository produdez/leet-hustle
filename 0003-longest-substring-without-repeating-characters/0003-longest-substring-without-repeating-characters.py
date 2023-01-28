class Solution:
    '''
        Version: 1
        
        Idea: Two pointers
        1. left/right points at sides of the non-duplicated string
        2. Loop through and
            - Check duplicate
            - Add new char to the unique dictionary
        3. When is duplicate !
            - Get + update maxLength
            - Remove all chars from 
                - Current duplicated index
                - To the current left
                From the unique dictionary
            - Move left pointer to right after the duplicated index
            - Override the duplicated index with the new index
        Complexity:
        - Time: O(n) loop through all once, pop out max n times
        - Space: O(n) could need to hold all n elements
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        uniq = {} # store unique char and it's index
        maxLen = 0
        for right, char in enumerate(s):
            if char in uniq:
                maxLen = max(maxLen, right - left) 
                for c in s[left: uniq[char]]:
                    uniq.pop(c)
                left = uniq[char] + 1
            
            # add new char or override index of duplicated char
            uniq[char] = right 
        return max(maxLen, len(s) - left)
