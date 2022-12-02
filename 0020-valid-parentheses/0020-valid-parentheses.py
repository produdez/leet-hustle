class Solution:
    '''
        Solution 2.1: Recursive Approach Updated
        Formatted 
    '''

    
    def isValid(self, test_string: str) -> bool:
        matching_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        is_right = lambda x: x not in matching_dict
        split = lambda string: (string[0], string[1:]) 
        
        def match_and_trim(starting_bracket: str, tail: str):
            '''
                Idea: You have a starting bracket and a string to match (tail) the bracket with
                This function try to match and trim matching pairs and return the unmatched

                If at a case that we cannot match and trim (unmatchable) we just return the full string
            '''
            # no string left to match -> return the start bracket
            if not tail: return starting_bracket
            # no starting bracket but have tail -> split and match the tail
            if not starting_bracket: return match_and_trim(*split(tail)) 
            # open char is right bracket -> un-matchable
            if is_right(starting_bracket): return starting_bracket + tail
            
            tail_head, tail_remain = split(tail)
            # if tail starts with a matching right bracket, keep trimming the remaining
            if is_right(tail_head) and matching_dict[starting_bracket] == tail_head: 
                return match_and_trim('', tail_remain)
            
            # else we just try to match and trim tail with itself
            trimmed_tail = match_and_trim(tail_head, tail_remain)
            
            # if the tail cannot be trimmed -> unmatchable
            if trimmed_tail == tail: return starting_bracket + tail

            # continue matching the trimmed tail with current starting_bracket
            return match_and_trim(
                starting_bracket, 
                trimmed_tail
            )
        
        # only case of success is when the string is matched and completely reduced to empty
        return match_and_trim('', test_string) == ''

            
            
        
        