class Solution:
    '''
        Idea:
        check if first digit == last digit 
        and then take the middle part out and repeat
        
        # Special case is when the middlepart have trailing zeros
        # Example: 1002011 -> mid=00201=201 -> not palin
            but 1002001 -> mid=00200-> 200  -> stil palin
    '''
    def isPalindrome(self, x: int) -> bool:
        def checkFirstLast(x):
            # NOTE: mag stands for magnitude order or floor(log10(x))
            magX = int(math.log10(x))
            last = x % 10
            first = x // (10**magX)

            if last != first: return None
            
            mid = (x % 10**magX) // 10
            if mid == 0: return 0

            magMid = int(math.log10(mid))
            if magMid != magX - 2: # this case is when the mid number has 0-trailings 
                n_trail = magX - 2 - magMid
                # even trailing 00011000
                if mid % (10** n_trail) == 0: return mid // (10**n_trail)
                
                return None # uneven trailing ex 0001011
            return mid

        if x==0: return True
        if x<0: return False # fuck this stupid case :)
        while True:
            x = checkFirstLast(x)
            if x is None: return False
            if x is 0: return True