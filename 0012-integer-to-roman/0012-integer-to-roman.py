class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
        
        roman_str = ''
        magnitude = 10 ** math.floor(math.log10(num))
        while magnitude > 0:
        # for magnitude in [10**i for i in range(math.floor(math.log10(num)), -1, -1)]:
            head_val = (num // magnitude) % 10

            if magnitude * head_val in roman_dict: 
                roman_str += roman_dict[magnitude * head_val]
            else:
                if head_val > 5:
                    roman_str += roman_dict[5 * magnitude] 
                    head_val -= 5
                
                roman_str += roman_dict[magnitude] * head_val
            
            magnitude //= 10
        
        return roman_str
            
            