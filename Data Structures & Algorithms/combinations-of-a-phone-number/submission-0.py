class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        combination = []


        reference = { "2": ["a", "b", "c"],
                      "3": ["d", "e", "f"],
                      "4": ["g", "h", "i"],
                      "5": ["j", "k", "l"],
                      "6": ["m", "n", "o"],
                      "7": ["p", "q", "r"],
                      "8": ["t", "u", "v"],
                      "9": ["w", "x", "z"]
                     }
        if not digits:
            return []
        def dfs(i): #
            if i == len(digits):
                res.append("".join(combination))
                return 

            #there are 3 choices every time 
            for char in reference[digits[i]]:
                combination.append(char)
                dfs(i+1)
                combination.pop()
            

        
        dfs(0)

        return res 




        