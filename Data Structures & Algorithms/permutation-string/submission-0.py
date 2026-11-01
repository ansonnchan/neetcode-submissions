class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        k = len(s1)

        for left in range(len(s2) - k + 1):
            #construct the substring
            substr = ""
            for i in range(left, left + k):
                substr += s2[i]
            if Counter(s1) == Counter(substr):
                return True

        
        return False