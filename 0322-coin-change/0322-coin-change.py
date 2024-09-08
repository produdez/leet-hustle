class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort() # small to large
        mem = {0: 0}
        def dp(target):
            if target < 0: return -1
            if target in mem: return mem[target]
            
            res = float('inf')
            for c in coins[::-1]:
                r = dp(target - c)
                if r < 0: continue
                res = min(1 + r, res)
            
            res = -1 if res == float('inf') else res
            mem[target] = res
            return res 
        dp(amount)
        

        # print(mem)
        return mem[amount]