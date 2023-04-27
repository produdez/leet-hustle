class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)  == 0: return 0
        if len(cost) == 1: return cost[0]
        one, two = cost[-1], cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            # print(i)
            temp = two
            two = cost[i] + min(one, two)
            one = temp
        return min(one, two)