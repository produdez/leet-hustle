class Solution:
    '''
        Version:
            Backtrack with DP memoize 1D
        Idea:
            Take each coin and also track best #coin taken (smallest)
            everything tracked in memoize function
        Complexity:
        - Time: O(m*d) reduced from O(m^d)
            with m being #coin and d is average depth of tree (how many coins are checked to reach result/deadend)
        - Space: O(d)
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memoize = {i: 1 for i in coins}
        
        def dfs(amount):
            if amount == 0: return 0
            if amount in memoize: return memoize[amount]
            
            best = math.inf
            for coin in coins:
                if amount < coin: break
                
                res = dfs(amount - coin) + 1
                if res > 0: best = min(res, best)
                if res == 1: break # early stop for best case
            
            if best == math.inf: best = -1
            memoize[amount] = best
            return best
        
        return dfs(amount)