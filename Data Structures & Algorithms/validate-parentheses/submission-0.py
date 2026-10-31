class Solution:
    def isValid(self, s: str) -> bool:
        #closing brackets
        references = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in "({[": #if it is an opening bracket
                stack.append(char)
            elif char in references: #closing
                if not stack or stack.pop() != references[char]:
                    return False
        
        return not stack 

    #O(n) space, O(n) time 


