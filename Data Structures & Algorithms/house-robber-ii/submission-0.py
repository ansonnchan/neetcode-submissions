class Solution:
    def rob(self, nums: List[int]) -> int:
        #this one is interesting, because now
        #we have an additional edge case in we have to check the first and last
        #initial approach doesn't differ much from house robbers I

        if len(nums) == 1:
            return nums[0]

        

        def helper(start, end):
            memo = [-1]*len(nums)
            
            def dfs(i):
                if i > end:
                    return 0

                if memo[i] != -1:
                    return memo[i]
                
                rob = nums[i] + dfs(i+2)
                skip = dfs(i+1)

                memo[i] = max(rob, skip)

                return memo[i]
            return dfs(start)
            
        return max(helper(0, len(nums)-2), helper(1, len(nums)-1))
            

        