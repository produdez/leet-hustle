from pprint import pprint
class Solution:
#     def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
#         invalid_counter = [set() for _ in range(n)]
#         for row,col in reservedSeats:
#             if col in [2,3,4,5]: invalid_counter[row-1].add(0)
#             if col in [6,7,8,9]: invalid_counter[row-1].add(1)
#             if col in [4,5,6,7]: invalid_counter[row-1].add(2)
        
#         result = 2 * n # max valid
#         for invalidated_count in invalid_counter:
#             value = len(invalidated_count)
#             if value == 3: result -= 2
#             elif value > 0: result -= 1
#         print(invalid_counter)
#         return result

	def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Just testing other's code

		seats = collections.defaultdict(set)

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
			else:
				res -= 1

		return res