class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occur = collections.defaultdict(int) # 0
        left = 0
        mostFreq = ''
        maxLen = 0
        for right, char in enumerate(s):
            occur[char] += 1
            if occur[char] > occur[mostFreq]:
                mostFreq = char
            
            strLen = (right - left + 1)
            if strLen - occur[mostFreq] <= k:
                maxLen = max(maxLen, strLen)
            else:
                occur[s[left]] -= 1
                left += 1
        return maxLen