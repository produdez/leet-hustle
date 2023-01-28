class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        uniq = {}
        maxLen = 0
        for right, char in enumerate(s):
            if char in uniq:
                maxLen = max(maxLen, right - left)
                for c in s[left: uniq[char]]:
                    uniq.pop(c)
                left = uniq[char] + 1
            uniq[char] = right
        return max(maxLen, len(s) - left)
