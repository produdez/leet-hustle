class Solution:
    '''
        (not finished)
        Solution 2: Recursive Approach
    '''

    
    def isValid(self, s: str) -> bool:
        matching_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        is_left = lambda x: x in matching_dict
        split = lambda string: (string[0], string[1:])

        def recur_valid(open_char, s):
            '''
                empty string: done
                None: fail
                some string: remaning
            '''

            if not open_char and not s: ''
            if not open_char: 
                open_char, s = split(s)
                if not is_left(open_char): return None
                return recur_valid(open_char, s)
            if not s: return None

            head, remain = split(s)
            if is_left(head): 
                return recur_valid(
                    open_char, 
                    recur_valid(head, remain)
                )
            if matching_dict[open_char] == head: return remain
            return None
        
        s = recur_valid(None, s)
        while(s != None and len(s) > 0):
            s = recur_valid(None,s)
        return s == ''

            
            
        
        