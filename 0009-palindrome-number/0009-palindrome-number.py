class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        
        magnitude = math.floor(math.log10(x))
        while magnitude > 0: 
            head = x // (10**magnitude)
            tail = x % 10
            if head != tail: return False
            
            x = x % (10**magnitude) // 10
            magnitude -= 2
        return True