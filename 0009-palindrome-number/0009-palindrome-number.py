class Solution:
    ''' 
        Idea 2
    
        Reverse the number and check 
        Actually, i want to reverse HALF of the number only
        2002 -> check if 02 reversed into 20 or not
        
        Also number of digit (even/odd) is a bitch
        # NOTE: reversing head not tail to make sure not bumping into trailing zeroes!!
        
    '''
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        if x==0: return True
        
        magOrder = int(math.log10(x))
        
        halfMagOrder = ((magOrder+1) // 2)
        tail = x % (10 ** halfMagOrder)
        head =  (x // (10** halfMagOrder) # odd digit
            if halfMagOrder * 2 != magOrder 
            else x // (10 ** (halfMagOrder + 1))) # even digit

        reversedHead = 0
        while head != 0:
            reversedHead = reversedHead * 10 + head % 10
            head = head // 10

        return tail == reversedHead