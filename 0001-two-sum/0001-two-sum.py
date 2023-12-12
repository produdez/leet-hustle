class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in visited: return [i, visited[complement]]
            visited[val] = i
        
        return False