class Solution:
    # sol note: use len and array index instead of enumerate
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = dict()
        for idx in range(len(nums)):
            number = nums[idx]
            complement = target - number
            if complement in bag: 
                return [idx, bag.get(complement)]
            bag[number] = idx
                