class Solution:
    '''
    
        Version: 3?
            I did not note the first few versions
            Dynamic with no edge cases
        Idea:
            - Cur_rob = Max(Prev_2_rob + curHOuse or Prev_1_rob)
            - Init prev, cur as 0 to remove 2 edge cases
            - use python built in swap for cleaner code
    '''
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for val in nums:
            prev, cur = cur, max(cur, prev + val)
        return cur