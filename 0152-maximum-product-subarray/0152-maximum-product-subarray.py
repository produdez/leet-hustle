class Solution:
    '''
        Note: version 1 bruteforce does not work fast enough
        Version 2:
            Trick :3
        Idea:
            Keep track of max and min of the tail of our current expanding
            subset
            Meaning what is the MIN/MAX of the longest 
            continuous subsetincluding the current element
            -> from that we can just expand and update best max
        Complexity:
        - Time: O(n)
        - Space: O(1)
    '''
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxx, minn = 1, 1
        
        for num in nums:
            if num == 0: 
                res = max(res, 0)
                maxx, minn = 1, 1
            elif num > 0:
                maxx = max(num, maxx * num)
                minn = min(num, minn * num)
                res = max(res, maxx)
            else:
                temp_max = maxx
                maxx = max(num, minn * num)
                minn = min(num, temp_max * num)
                res = max(res, maxx)
                            
        return res