class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #brute force approach
        #median is the middle
        #if odd, direct middle, if even, median is sum of 2 middles divided by 2 

        #we create new array, combine
        # then find the median

        combined = []

        #it doesn't matter which length of array to choose
        #because once an array length ends, the rest will be bigger so just append
        
        i, j = 0,0 
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
        #append remaining
        while i < len(nums1):
            combined.append(nums1[i])
            i += 1

        while j < len(nums2):
            combined.append(nums2[j])
            j += 1

        #find median
        if len(combined)%2 == 0:
            return (combined[len(combined) // 2 - 1] + combined[len(combined) // 2]) / 2
        else: 
            return combined[len(combined)//2]
            
        