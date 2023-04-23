class Solution:
    '''
        Version: 2
            More intuitive
        Idea:
            Perm(listN) = fixed_position_character + perm(listN - character)
            for every char in listN
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(perm = [], nums= []):
            if not nums: return [perm]
            
            res = []
            for i in range(len(nums)):
                res += dfs(perm + [nums[i]], nums[:i] + nums[i+1:])
            return res
        
        return dfs([], nums)