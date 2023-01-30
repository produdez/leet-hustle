class Solution:
    '''
        Version: 3.5
            A bit more optimization with the bigbrain freq check
        Idea: Same as version 2 (window moving) with optimization
            A window represent substr [left, right]
            -> valid: len(wind) - maxFreq <= k -> update maxLen
            -> else: move left pointer til valid
        Optimization: No need to get maxFreq every loop 
            (reduce condition check from O(m) -> O(1))
            m is #unique_char (this case 26)
        Complexity:
        - Time: O(2n) -> O(n)
            window expand right n times
            window strink left maximum ~n time
        - Space: O(n) for occurance HashMap
        * NOTE: <big-brain>
            WHY dont we update maxFrequency when strinking window?
            --
            Because 
            1. we're looking for the maxLen valid string here
            2. maxFreq decreasing only make the tring more invalid
            --
            The only way that we find another maxLength str is when
            there's a string with more duplicated element
            AKA when maxFreq is increased
            -- <update>
            Also, there's no need to strink window but just shift it
            when invalid bc strinking the window does not give us a better
            result !!! (maxLen will never be updated)
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        occur = collections.defaultdict(int)
        maxLen = 0
        maxFreq = 0
        for right, rChar in enumerate(s):
            occur[rChar] += 1
            maxFreq = max(maxFreq, occur[rChar])
            
            if (right - left + 1) - maxFreq > k:
                occur[s[left]] -= 1
                left += 1
                # no need update maxFreq
            maxLen = max(maxLen, right - left + 1)

        return maxLen