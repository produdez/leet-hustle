class Solution:
    def countBits(self, n: int) -> List[int]:
        # Simple Sol
        
        if n == 0: return [0]
        cur, nxt = 0, 2
        arr = [0,1]
        for i in range(2, n+1):
            if i == nxt:
                cur = nxt
                nxt = nxt * 2
                arr.append(1)
            else:
                arr.append(1 + arr[i-cur])
        return arr