class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        

        for i in tokens:
            if i in "+-/*":
                op2 = stack.pop()
                op1 = stack.pop()

            if i == "+":
                stack.append(op1 + op2)
            elif i == "-":
                stack.append(op1-op2)
            elif i == "*":
                stack.append(op1*op2)
            elif i == "/":
                stack.append(int(op1/op2))
            else:
                stack.append(int(i))
        
        return stack[-1]

