import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Version 1
            
            Idea:
                Keep a sorted MIN heap of temperature and their respective index
                Ilterate the temperature array and
                    - When current temp > heap head temp (meaning has results)
                    - We keep poping the heap and get the index difference
                    - Then we put the current (temp, index) into the heap
            Complexity:
            - Time: O(n*(log(n)))
            - Space: O(n) result array + O(n) heap 
                -> O(n) 
        '''
        heap = [] # heap of tuple (temperature, index)
        for index, temp in enumerate(temperatures):
            while heap and heap[0][0] < temp:
                head = heapq.heappop(heap)
                temperatures[head[1]] = index - head[1]
            
            heapq.heappush(heap, (temp, index))
        
        for _, i in heap:
            temperatures[i] = 0
        return temperatures
            