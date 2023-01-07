class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Version: 1
            
            Count into a HashMap
            and sort the keys by value and return k elements
            
            Complexity:
                Time: O(n)-Count + O(mlogm)-Sort (m is #unique values)
                    -> Total O(mlogm)
                Space: O(n)-HashMap + anythat sorting cause (posbiliy O(1))
        '''
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        sorted_key = sorted(counter.keys(), key=counter.get, reverse=True)
        return sorted_key[:k]