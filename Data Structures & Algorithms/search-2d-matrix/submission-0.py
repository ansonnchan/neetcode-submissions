class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #want to search the max of each row (so the last)
        #if target > last, we move next, if target <, it is the row
        #the ndo binary search until we get it

        #in fact, we can probably do binary search twice

        #let's try both ways 

        #sol 1: brute force double for loops 

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    return True
        
        return False