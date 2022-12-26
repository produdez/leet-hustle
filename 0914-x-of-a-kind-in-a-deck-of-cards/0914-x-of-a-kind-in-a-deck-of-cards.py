class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        grouping = {}
        for card in deck:
            if card in grouping:
                grouping[card] += 1
            else:
                grouping[card] = 1
        
        numbers = list(grouping.values())
        if len(numbers) < 2: return numbers[0] > 1
        
        
        # Note grouping value could be 2 rather than 4 and 3 rather than 9
        # find that number
        gcd = math.gcd(numbers[0], numbers[1])
        if gcd == 1: return False
        print(gcd, numbers)
        for num in numbers:
            gcd = math.gcd(gcd, num)
            if gcd < 2: return False
        return True
            
            
        