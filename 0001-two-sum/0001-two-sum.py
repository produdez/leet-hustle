class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = dict()
        for (idx, n1) in enumerate(nums):
            n2 = target - n1
            if n2 in bag: 
                return [idx, bag.get(n2)]
            bag[n1] = idx
                