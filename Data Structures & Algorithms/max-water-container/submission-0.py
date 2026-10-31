class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #l,r pointer
        #we compute max at that time (like greedy)
        #we move the lower of the heights
        #then compute 
        max_Area = 0
        left, right = 0, len(heights)-1
        while left < right:
            curr_width = right - left
            curr_height = min(heights[left],heights[right])
            curr_Area = curr_width*curr_height
            max_Area = max(max_Area, curr_Area)

            #if we're moving inwards anyways, we want the max height
            if heights[left]>heights[right]:
                right-=1
            elif heights[left]<heights[right]:
                left+=1
            else:#if they're equal, then it doesn't really matter
                #arbitary pick left+=1
                left+=1
        return max_Area
