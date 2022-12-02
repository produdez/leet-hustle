class Solution:
    '''
        (have not cleaned up)
        Solution 2.1: Recursive Approach Updated
    '''

    
    def isValid(self, test_string: str) -> bool:
        matching_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        is_left = lambda x: x in matching_dict
        split = lambda string: (string[0], string[1:])
        
        def recur_valid(open_char, s):
            # print(open_char, s)
            if not open_char and not s: return ''
            if not open_char: 
                open_char, s = split(s)
                if not is_left(open_char): return open_char + s
                return recur_valid(open_char, s)
            if not s: return open_char

            head, remain = split(s)
            if is_left(head): 
                matching_tail = recur_valid(head, remain)
                if matching_tail == s:
                    return open_char + s
                else:
                    return recur_valid(
                        open_char, 
                        matching_tail
                    )
            if matching_dict[open_char] == head: return recur_valid(None, remain)
            return open_char + s
        
        # print('starting: ', test_string)
        return recur_valid(None, test_string) == ''

            
            
        
        