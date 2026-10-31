class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #[1,2,3,4] -> 1234 
        # add to sum so 1235
        #and then split back into [1,2,3,5]

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits