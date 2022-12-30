from pprint import pprint
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat_rep = {}
        for r,c in reservedSeats:
            if c == 1 or c == 10: continue
            if not(r in seat_rep): seat_rep[r] = 0b111

            if c in [2,3,4,5]: seat_rep[r] &= ~(1 << 2)
            if c in [4,5,6,7]: seat_rep[r] &= ~(1 << 1)
            if c in [6,7,8,9]: seat_rep[r] &= ~(1 << 0)

        result = n*2
        for rep in seat_rep.values():
            if rep == 0b0: result -= 2
            else: result -= 1
        return result