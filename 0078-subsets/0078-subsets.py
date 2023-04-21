class Solution:
    '''
        Version 2:
            DFS properly
        
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def add(nums, start=[]):
            if not nums: 
                nonlocal result
                result.append(start)
                return
            
            add(nums[1:], start + [nums[0]])
            add(nums[1:], start)
            
        add(nums)
        return result