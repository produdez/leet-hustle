class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
            
        result = []
        for _ in range(len(nums)):
            exclude = nums.pop(0)
            
            permute_excluded = self.permute(nums)
            result.extend([perm + [exclude] for perm in permute_excluded])
            
            nums.append(exclude)
        
        return result