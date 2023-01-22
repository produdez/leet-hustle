class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            Version 1:
            
            Idea: 
            Binary search from 1 to max speed
            
            1. Right points to max_valid value
            2. left points to small potentially invalid values
            When searching, we keep updating the left, ignoring all the invalid values 
            While for the right, we keep the last valid value 
            and when pivot meets left, right, we stop
            
            Intiution:
            When searching, if speed is too slow, means it's invalid
                -> move to the right
            If speed is fast (good)
                -> move to the left but keep the current pivot as the right so that we khow the last valid value is our current right
            -> result stop when left = right = piv
        '''
        left, right = 1, max(piles)
        def calc_time(speed):
            eat_time = 0
            for p in piles:
                eat_time += math.ceil(p/speed)
            return eat_time
        
        i = 0
        while True:
            i += 1
            pivot = (left + right) // 2
            eat_time = calc_time(speed=pivot)
            if pivot == left == right: break
            if eat_time > h:
                left = pivot + 1
            else:
                right = pivot
        return pivot
                