class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #l, r pointer at the beginning
        #if no duplicate, move right across, 
        #if duplicate, reset count, move left to right and repeat
        
        longest = 0 

        left, right = 0,0

        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                seen.remove(s[left])
                left+=1
        
        return longest
            
            

        