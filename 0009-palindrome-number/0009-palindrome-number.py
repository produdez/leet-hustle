class Solution:
    ''' 
        Update Idea 1
        
        still left right check 
        but now more elegant and not care about trailing zero in mid section anymore
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        
        magnitude = 10 ** int(math.log10(x))
        mid = x
        while mid:
            print(mid)
            left = mid // magnitude
            right = mid % 10
            if left != right: return False

            mid = (mid % magnitude) // 10
            magnitude = magnitude // 100
            # elegance here where your mid could be
            # number like 0002101 with magnitude 100000 
            # which makes the trailing 0 still valid 
        return True