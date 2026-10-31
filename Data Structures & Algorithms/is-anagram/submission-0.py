class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #technically, we don't need this length check,
        # but in a real world scenario, would help 
        # to compute immediate wrong answers 

        if len(s) != len(t):
            return False 
        
        return Counter(s) == Counter(t)
        
        #O(n) space, O(n) time 