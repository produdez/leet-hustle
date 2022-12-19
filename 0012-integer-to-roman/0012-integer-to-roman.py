class Solution:
    def intToRoman(self, num: int) -> str:
        '''
            Version 2
            
            Idea: Instead of looping throught the number,
            loop the greek dictionary instead
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
        for val, char in reversed(roman_dict.items()):
            roman_str += char * (num // val)
            num %= val
        return roman_str
            
            