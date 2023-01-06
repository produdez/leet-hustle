class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Version: 1
            
            Idea:
            
            Have a matching dicitonary that maintain the count 
            of every character
            - char from s -> +1
            - char from t -> -1
            So after adding all chars, all dictionary's entry must be 0
            
            Complexity:
            
            Time: 
                O(n) (loop) + O(m) (check sum) -> O(n)
                with n being #char m being #unique_chars
            Space:
                O(m) for the dict
        '''
        if len(t) != len(s): return False
        
        match = {}
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s in match:
                match[char_s] += 1
            else:
                match[char_s] = 1
            
            if char_t in match:
                match[char_t] -= 1
            else:
                match[char_t] = -1
        
        for val in match.values():
            if val != 0: return False
        return True
        