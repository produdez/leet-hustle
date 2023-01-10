import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Version 2
            
            Idea: Use a monotonic decresing stack
            Complexity:
            - Time: O(n)
            - Space: O(n)
        '''
        
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j, _ = stack.pop()
                temperatures[j] = i - j
                
            stack.append((i,temp))
        
        for i, _ in stack:
            temperatures[i] = 0
        return temperatures