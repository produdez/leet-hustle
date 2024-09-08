class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        def binary(l,r):
            if l > r: return -1
            m = (l + r) // 2
            
            a,b,c = nums[l], nums[m], nums[r]
            if a == target: return l
            if b == target: return m
            if c == target: return r
            
            if a <= b:
                if a < target < b:
                    return binary(l, m)
                else:
                    return binary(m+1, r)
            else:
                if b < target < c:
                    return binary(m+1, r)
                else:
                    return binary(l, m)

        return binary(l,r)