class Solution:
    '''
        Version: 2
            Bottom up DP
        Idea:
            Work up from amount = 0 to amount = n
        Complex:
            Time: O(n * m) n~amount and m is avg#coin taken aka depth
            Space: O(n)
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort()
        memoize = {i: 1 for i in coins}
        memoize[0] = 0
        
        def bottomUp(amount):
            if amount in memoize: return amount
            
            res = math.inf
            for coin in coins:
                if amount < coin: break
                if amount - coin in memoize:
                    res = min(memoize[amount - coin] + 1, res)
            
            if res != math.inf: memoize[amount] = res
        
        for i in range(1, amount + 1):
            bottomUp(i)
        
        if amount in memoize: return memoize[amount]
        return -1