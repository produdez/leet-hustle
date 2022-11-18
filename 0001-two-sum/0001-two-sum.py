class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_bag = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in key_bag: return [i, key_bag.get(complement)]
            key_bag[num] = i
        
        raise Exception('No pair ever add up to the target')