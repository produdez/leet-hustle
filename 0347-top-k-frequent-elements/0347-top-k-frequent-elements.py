class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        sorted_key = sorted(counter.keys(), key=counter.get, reverse=True)
        return sorted_key[:k]