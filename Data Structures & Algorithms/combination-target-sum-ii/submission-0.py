class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #have duplicates
        candidates.sort()
        res = []
        combination = []

        def dfs(i, total):
            if total == target:
                res.append(combination.copy())
                return
            
            if i == len(candidates) or total > target:
                return #incorrect
            
            #choice 1: include candidates[i]
            combination.append(candidates[i])
            dfs(i+1, total + candidates[i])
            combination.pop()

            #choice 2: exclude candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i+1, total)

        dfs(0, 0)

        return res

