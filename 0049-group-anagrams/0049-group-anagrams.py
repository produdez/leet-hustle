class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Version 3
            group by sorting
            
            NOTE: This version complexity is O(n * mlog(m)) 
                m being avg str length
                n is #str
            ** This is best performer in this site's result since m is very small (<100)**
        '''
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(''.join(sorted(s)))].append(s)
        return groups.values()