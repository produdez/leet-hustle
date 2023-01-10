import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        heap = []
        for i, num in enumerate(temperatures):
            while heap and heap[0][0] < num:
                head = heapq.heappop(heap)
                result[head[1]] = i - head[1]
            
            heapq.heappush(heap, (num, i))
        
        for num, i in heap:
            result[i] = 0
        return result
            