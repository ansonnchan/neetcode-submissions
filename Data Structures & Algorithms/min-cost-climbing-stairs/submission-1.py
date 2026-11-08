class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1]*len(cost) #this contains min cost from each step

        def dfs(i):
            if i >= len(cost):
                return 0 
            if memo[i] != -1: #we have already computed 
                return memo[i]
            #else
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return memo[i]
        
        return min(dfs(0), dfs(1))