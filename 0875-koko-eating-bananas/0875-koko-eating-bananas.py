class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        print('max: ', right, ' time_limit: ', h)
        def calc_time(speed):
            eat_time = 0
            for p in piles:
                eat_time += math.ceil(p/speed)
            return eat_time
        
        # for i in range(math.ceil(math.log2(right))):
        i = 0
        while True:
            # print(f'-- {i} -------')
            i += 1
            pivot = (left + right) // 2
            eat_time = calc_time(speed=pivot)
            # print(f'left: {left}, right: {right}, piv: {pivot}')
            # print('time: ', eat_time)
            if pivot == left == right: break
            if eat_time > h:
                left = pivot + 1
            else:
                right = pivot
        return pivot
                