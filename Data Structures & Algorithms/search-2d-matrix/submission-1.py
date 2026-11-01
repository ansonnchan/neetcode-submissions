class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #want to search the max of each row (so the last)
        #if target > last, we move next, if target <, it is the row
        #the ndo binary search until we get it

        #in fact, we can probably do binary search twice

        #let's try both ways 

        #sol 2: binary search to find 
        left, right = 0, len(matrix) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if matrix[middle][-1] < target:
                left = middle + 1
            else:
                right = middle - 1

        # Check if a valid row exists
        if left >= len(matrix):
            return False

        row = matrix[left]

        # Now iterate through that row
        for num in row:
            if num == target:
                return True

        return False

        #this approach gives us O(1) space, O(n+O(logm))
        