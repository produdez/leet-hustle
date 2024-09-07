class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start,end = 0, 1
        max_profit = 0
        while end < len(prices):
            profit = prices[end] - prices[start]
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                start = end
            end += 1
        
        return max_profit