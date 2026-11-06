class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def dfs():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return 

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    dfs()
                    permutation.pop()
                        
        dfs()
        return res