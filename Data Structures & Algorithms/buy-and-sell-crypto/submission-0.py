class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                max_profit = max(max_profit, sell-buy)
        return max_profit 

        #brute force: O(n^2) time, O(1) space
            
        
        


        