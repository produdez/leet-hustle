class Solution:
    '''
        Version: 1
        
        Idea:
            At every pivot, there can only be two cases
            1. pivot > left -> means left to pivot is ordered
                So we just check if target is between those and
                - Yes -> binary search from left to piv
                - No -> shift left pointer
            2. pivot < right -> right to piv is ordered
                Same
                - Between -> bin search
                - Not -> shift right pointer
            So basically this is just advanced binary search
        Complexity:
        - Time: O(log(n)) for sure
        - Space: O(1)
    '''
    def search(self, nums: List[int], target: int) -> int:        
        def binarySearch(l, r):
            while l <= r:
                piv = (l+r) // 2                
                if nums[piv] == target: return piv
                
                if nums[piv] < target:
                    l = piv + 1
                else:
                    r = piv - 1
            return -1
        
        between = lambda a, b: a <= target and target <= b
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            nL, nR, nP = nums[left], nums[right], nums[pivot]
            if nP == target: return pivot
            
            if nP >= nL: 
                if between(nL, nP):
                    return binarySearch(left, pivot - 1)
                else:
                    left = pivot + 1
            else:
                if between(nP, nR):
                    return binarySearch(pivot + 1, right)
                else:
                    right = pivot - 1
        return -1 
                