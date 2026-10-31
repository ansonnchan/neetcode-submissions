class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non-decreasing -> ascending 
        #1-indexed so just add 1 to indices
        #index1 < index2
        left, right = 0, len(numbers)-1

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            elif curr > target:
                right -=1
            else:
                left+=1
            
        