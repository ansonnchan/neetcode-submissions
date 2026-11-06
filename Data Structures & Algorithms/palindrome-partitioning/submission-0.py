class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindrome = []

        def dfs(i):
            if i == len(s):
                res.append(palindrome.copy())
                return

            for j in range(i, len(s)):
                substr = s[i:j+1]

                if substr == substr[::-1]:
                    palindrome.append(substr)
                    dfs(j+1)
                    palindrome.pop()

        dfs(0)
        return res