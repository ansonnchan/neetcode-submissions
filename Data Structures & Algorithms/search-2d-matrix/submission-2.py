class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #want to search the max of each row (so the last)
        #if target > last, we move next, if target <, it is the row
        #the ndo binary search until we get it

        #in fact, we can probably do binary search twice

        #let's try both ways 

        #sol 3: two binary search to find 
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

        #now we do binayr search on the row

        left, right = 0, len(matrix[0])
        while left <= right:
            middle = left + (right-left)//2
            if row[middle] < target:
                left = middle + 1
            elif row[middle] > target:
                right = middle-1
            else:
                return True

        return False