class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        def binarySearch(l, r):
            print('Binary searching between: ', nums[l], nums[r])
            while l <= r:
                piv = (l+r) // 2
                # print(nums[l], nums[r], nums[piv])
                
                if nums[piv] == target: return piv
                
                if nums[piv] < target:
                    l = piv + 1
                else:
                    r = piv - 1
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            nL, nR, nP = nums[left], nums[right], nums[pivot]
            print('l,r,p: ', nL, nR, nP)
            if nP == target: return pivot
            
            if nP >= nL: 
                if nL <= target and target < nP:
                    return binarySearch(left, pivot - 1)
                else:
                    left = pivot + 1
            else:
                if nP < target and target <= nR:
                    return binarySearch(pivot + 1, right)
                else:
                    right = pivot - 1
        return -1 
                