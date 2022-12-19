class Solution:
    def intToRoman(self, num: int) -> str:
        '''
            Version 1
            
            Idea: get each char and convert it using a dictionary
            Note the case of >5 and <=5
            Also note that while loop and for loop does not have significant changes
        '''
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
        for magnitude in [10**i for i in range(math.floor(math.log10(num)), -1, -1)]:
            head_val = (num // magnitude) % 10

            if magnitude * head_val in roman_dict: 
                roman_str += roman_dict[magnitude * head_val]
            else:
                if head_val > 5:
                    roman_str += roman_dict[5 * magnitude] 
                    head_val -= 5
                
                roman_str += roman_dict[magnitude] * head_val        
        return roman_str
            
            