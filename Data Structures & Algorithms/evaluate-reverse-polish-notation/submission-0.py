class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #expression is valid so no need to worry about 
        #e.g. "[*,2,2]" or [2,*,2]
        numbers = []
        operations = "+-*/"

        for c in tokens:

            if c not in operations:
                numbers.append(int(c))
            
            else:
                num2 = numbers.pop()
                num1 = numbers.pop()

                if c == "+":
                    ans = num1 + num2
                elif c == "-":
                    ans = num1 - num2
                elif c == "*":
                    ans = num1 * num2
                else:
                    ans = int(num1 / num2)

                numbers.append(ans)

        return numbers[-1]
