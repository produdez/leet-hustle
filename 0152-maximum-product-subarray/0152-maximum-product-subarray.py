class Solution:
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