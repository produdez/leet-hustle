import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Version 2.1
                Optimize with only storing index in stack
            
            Idea: Use a monotonic decresing stack
            Complexity:
            - Time: O(n)
            - Space: O(n)
        '''
        
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                temperatures[j] = i - j
                
            stack.append(i)
        
        for i in stack:
            temperatures[i] = 0
        return temperatures