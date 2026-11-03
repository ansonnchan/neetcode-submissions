class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        for k in range(1, max(piles) + 1):
            count = 0

            for pile in piles:
                count += (pile + k - 1) // k

            if count <= h:
                return k