class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        def binary(l,r):
            if l > r: return -1
            m = (l + r) // 2
            
            a,b,c = nums[l], nums[m], nums[r]
            if b == target: return m
            
            if a <= b:
                if target < a or target > b:
                    return binary(m+1, r)
                else:
                    return binary(l, m)

            else:
                if target < b or target > c:
                    return binary(l, m)
                else:
                    return binary(m+1, r)
                    

        return binary(l,r)