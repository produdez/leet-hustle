class Solution:
    def countBits(self, n: int) -> List[int]:
        # bit manip
        if n == 0: return [0]
        arr = [0,1]
        for i in range(2, n+1):
            arr.append(arr[i>>1] + i%2)
        
        return arr