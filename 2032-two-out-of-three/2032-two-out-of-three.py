class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        for nums in [nums1, nums2, nums3]:
            nums.sort()
        result = []
        
        prev = None
        for i in range(len(nums1)):
            num = nums1[i]
            if num == prev: continue
            if num in nums2 or num in nums3:
                if num in result: continue
                result.append(num)
            prev = num
        
        prev = None
        for i in range(len(nums2)):
            num = nums2[i]
            if num == prev: continue
            if num in nums1 or num in nums3:
                if num in result: continue
                result.append(num)
            prev = num
        
        prev = None
        for i in range(len(nums3)):
            num = nums3[i]
            if num == prev: continue
            if num in nums1 or num in nums2:
                if num in result: continue
                result.append(num)
            prev = num

        return result