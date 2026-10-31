class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False 
        
        #method to break down easily 
        def split(num):
            ans = []
            while num > 0:
                ans.append(num%10)
                num //= 10
            return ans [::-1]

        seen = set()

        while n > 0:
            temp_sum = 0
            for num in split(n):
                temp_sum += num*num
            if temp_sum == 1:
                return True 
            if temp_sum in seen:
                return False
            seen.add(temp_sum)
            n=temp_sum 
        
        return True 
            




        
