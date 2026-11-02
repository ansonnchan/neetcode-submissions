class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #trivial solution is using counter and go throuhg
        #but that would be O(n) time and space

        freq = Counter(nums)

        for num, count in freq.items():
            if count == 1:
                return num
        
        
        