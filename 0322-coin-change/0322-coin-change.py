class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort()
        memoize = {i: 1 for i in coins}
        memoize[0] = 0
        
        def dfs(amount):
            if amount in memoize: return memoize[amount]
            
            best = math.inf
            for coin in coins:
                if amount < coin: continue
                remain = amount - coin
                
                res = dfs(remain) + 1
                if res > 0: best = min(res, best)
            
            memoize[amount] = -1 if best == math.inf else best
            return memoize[amount]

        return dfs(amount)