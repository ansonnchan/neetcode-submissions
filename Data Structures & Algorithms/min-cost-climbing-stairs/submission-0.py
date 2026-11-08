class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #at any step, we climb 1 or 2 steps
        #from each step, choose least 
        min_cost = 0

        def dfs(i): #returns cost 
            if i >= len(cost):
                return 0 #we've reached the top
            
            return cost[i] + min(dfs(i+1), dfs(i+2))

        
        return min(dfs(0), dfs(1))
        
        