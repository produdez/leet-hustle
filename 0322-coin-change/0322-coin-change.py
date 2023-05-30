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
        if amount == 0: return 0
        coins.sort()
        memoize = {i: 1 for i in coins}
        memoize[0] = 0
        
        def dfs(amount):
            if amount in memoize: return memoize[amount]
            
            best = math.inf
            for coin in coins:
                # cant take coin in smaller order -> cant take anything
                if amount < coin: break 

                res = dfs(amount - coin) + 1
                if res > 0: best = min(res, best)
            
            memoize[amount] = -1 if best == math.inf else best
            return memoize[amount]
        
        return dfs(amount)