class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lseq = [nums[0]]
        lsum = lseq[-1]

        end_idx = 0
        for i in range(1, len(nums)):
            if lseq[-1] != nums[i] - 1: 
                break
            
            lseq.append(nums[i])
            lsum += nums[i]
            end_idx = i
        # print(end_idx, lseq, lsum)
        missing = lsum
        pool = set(nums[end_idx:])
        while missing in pool: missing += 1
            
        return missing