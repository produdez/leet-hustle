class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Version: 1.5
                Rewrite with dict.get
            
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
            match[s[i]] = match.get(s[i], 0) + 1
            match[t[i]] = match.get(t[i], 0) - 1

        for val in match.values():
            if val != 0: return False
        return True
        