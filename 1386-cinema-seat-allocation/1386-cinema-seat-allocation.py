from pprint import pprint
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
# invalid_counter = {i+1 :set() for i in range(n)}
#         invalid_counter = collections.defaultdict(set)
#         for row,col in reservedSeats:
#             if col == 1 or col == 10: continue
#             if col in [2,3,4,5]: invalid_counter[row].add(0)
#             if col in [6,7,8,9]: invalid_counter[row].add(1)
#             if col in [4,5,6,7]: invalid_counter[row].add(2)
        
#         result = 2 * n # max valid
#         for i in invalid_counter:
#             count = len(invalid_counter[i])
#             if count == 3: result -= 2
#             elif count > 0: result -= 1
                
#         return result

        seats = collections.defaultdict(set)
        # seats = {i+1 :set() for i in range(n)}
        
        for i,j in reservedSeats:
            if j in [2,3,4,5]:
                seats[i].add(0)
            if j in [4,5,6,7]:
                seats[i].add(1)
            if j in [6,7,8,9]:
                seats[i].add(2)
        res = 2*n
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            elif len(seats[i]) > 0:
                res -= 1

        return res