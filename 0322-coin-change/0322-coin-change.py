class Solution:
    '''
        Version: 2.5
            Bottom up DP
            Update:
            - Use array with amount + 1 as MAX
            - No need to pre-initialize since that will happen
                as we bottom up and amount = 0
        Idea:
            Work up from amount = 0 to amount = n
        Complex:
            Time: O(n * m) n~amount and m is avg#coin taken aka depth
            Space: O(n)
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        memoize = [amount + 1] * (amount + 1)
        memoize[0] = 0
        coins.sort()
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt < coin: break
                # dont even need to check if it's in memoize
                # cause amt - coin always in memoize is amt >= coin
                    
                # this is possible since we go bottom up and if 
                # mem[amt-coin] is not found means it's MAX and max + 1 
                # is always larger than our current memoize[amt]
                memoize[amt] = min(memoize[amt-coin] + 1, memoize[amt])
                if memoize[amt-coin] == 0: break # best case
            
        
        return memoize[amount] if memoize[amount] != amount + 1 else -1