class Solution:
    '''
        Version: 2
        
        Idea:
        
        Complexity:
        Time: O(n * m) where m is #unique chars (this case 26)
        Space: O(n) for the occurence dictionary
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        occur = collections.defaultdict(int) # 0
        maxLen = 0
        for right, rChar in enumerate(s):
            occur[rChar] += 1
            maxFreq = max(occur.values()) # O(m=26)
            # print('.....')
            while right - left + 1 - maxFreq > k: #invalid
                # print(occur)
                occur[s[left]] -= 1
                left += 1
                maxFreq = max(occur.values())
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
                