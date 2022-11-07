class Solution:
    def checkFirstLast(self, x):
        magnitudeOrder = int(math.log10(x))
        last = x % 10
        first = x // (10**magnitudeOrder)
        
        if last != first: return None
        mid = (x % 10**magnitudeOrder) // 10
        if mid == 0: return 0
        
        magMid = int(math.log10(mid))
        if magMid != magnitudeOrder - 2: 
            # this case is when the mid number has 0-trailings 
            trailMag = magnitudeOrder - 2 - magMid
            if mid % (10** trailMag) == 0: 
                # even trailing 00011000
                return mid // (10**trailMag)
            return None # uneven trailing ex 0001011
        return mid
    def isPalindrome(self, x: int) -> bool:
        if x==0: return True
        if x<0: return False # fuck this stupid case :)
        while True:
            print('x: ', x)
            x = self.checkFirstLast(x)
            if x is None: return False
            if x is 0: return True