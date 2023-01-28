class Solution:
    '''
        Version: 2
        
        Idea: Expanding Window
        1. Keep a window containing the current non-dup string
            And also a set of all elements
        2. When encounter a duplicate
            * Strink the window from the left while popping the set
            Until duplicate is removed
        3. Update maxLength and add new element
        
        Note:
            Why pop from the left:
            Cause when an index i cause a duplicate at j
            We need to pop all before j and j
        Complexity:
        - Time: O(n) loop through all once, pop out max n times
        - Space: O(n) could need to hold all n elements
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        maxLen = 0
        uniq = set()
        for right in range(0, len(s)):
            while s[right] in uniq:
                uniq.remove(s[left])
                left += 1

            uniq.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen