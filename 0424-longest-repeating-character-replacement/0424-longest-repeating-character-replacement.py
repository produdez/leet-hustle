class Solution:
    '''
        Version: 2
        
        Idea: Simple expanding window
            A window [left, right] represent a sub string
            Valid if len(window) - frequency(most_occur_char) <= k
            1. So when invalid
                - Strink window from the left 
                - And update occurance/maxFreq
            2. Till it's valid
                - Update max len
            3. Also note to update occur/max Freq when expanding window

        Complexity:
        Time: O(2 * n * m) where m is #unique chars (this case 26)
            Every char is added in once
            Every char could be popped out once
            -> 2n
            Each time add/pop -> update takes m 
            -> 2n * m
        Space: O(n) for the occurence dictionary
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        occur = collections.defaultdict(int) # 0
        maxLen = 0
        for right, rChar in enumerate(s):
            occur[rChar] += 1
            maxFreq = max(occur.values()) # O(m=26)
            
            while right - left + 1 - maxFreq > k: #invalid
                occur[s[left]] -= 1
                left += 1
                maxFreq = max(occur.values())
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
                