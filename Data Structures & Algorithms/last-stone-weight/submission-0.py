class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        sorted_stones = sorted(stones)

        while len(sorted_stones) > 1:
            y = sorted_stones.pop()  # largest
            x = sorted_stones.pop()  # second largest

            if x != y:
                sorted_stones.append(y - x)
                sorted_stones.sort()

        return sorted_stones[0] if sorted_stones else 0