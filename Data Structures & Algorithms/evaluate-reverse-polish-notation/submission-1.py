class Solution:
    import math
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range (len(tokens)):
            if tokens is None:
                return count  
            elif tokens[i]=="+" and stack:
                
                stack.append(stack.pop()+stack.pop())
            elif tokens[i]=="-" and stack:
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif tokens[i]=="*":
    
                stack.append(stack.pop()*stack.pop())
            elif tokens[i]=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]