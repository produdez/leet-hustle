from pprint import pprint
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # invalid_counter = {i+1 :set() for i in range(n)}
        invalid_counter = collections.defaultdict(set)
        for row,col in reservedSeats:
            if col == 1 or col == 10: continue
            if col in [2,3,4,5]: invalid_counter[row].add(0)
            if col in [6,7,8,9]: invalid_counter[row].add(1)
            if col in [4,5,6,7]: invalid_counter[row].add(2)
        
        result = 2 * n # max valid
        for i in invalid_counter:
            
            match len(invalid_counter[i]):
                case 3: result -= 2
                case 0: continue
                case _: result -= 1
                
        return result