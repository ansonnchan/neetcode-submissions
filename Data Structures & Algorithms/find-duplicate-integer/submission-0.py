class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #the trivial solution is creating a counter and 
        #iterating through it

        freq = Counter(nums)

        for k,v in freq.items():
            if v > 1:
                return k
        