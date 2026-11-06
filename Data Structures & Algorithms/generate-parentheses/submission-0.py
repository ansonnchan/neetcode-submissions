class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        good = []

        def dfs(open, close):
            if open == n and close == n:
                res.append("".join(good))
                return 
            
            #choice 1: append (
            if open < n:
                good.append("(")
                dfs(open+1, close)
                good.pop()
            
            #choice 2: add closing )
            if close < open:
                good.append(")")
                dfs(open, close+1)
                good.pop()


        dfs(0,0)

        return res

        