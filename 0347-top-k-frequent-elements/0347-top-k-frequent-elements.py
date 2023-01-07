class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Version: 2 
                update sort with bucket sort
            
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
        
        # each index in bucket represents the frequency
        count_buckets = [[] for _ in range(len(nums))]
        for num, freq in counter.items():
            count_buckets[len(nums) - freq].append(num)
        
        result = []
        for bucket in count_buckets:
            for num in bucket:
                if k==0: return result
                result.append(num)
                k -= 1
        return result