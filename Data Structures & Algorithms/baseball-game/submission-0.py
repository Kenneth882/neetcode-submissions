class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        x=0
        stack=[]
        for i in range(len(operations)):
            if operations[i] == "+":
                val=stack[-1]+stack[-2]
                val=int(val)
                stack.append(val)
            elif operations[i] =="C":
               stack.pop()
            elif operations[i]=="D":
                val=stack[-1]*2
                val=int(val)
                stack.append(val)
            else:
                stack.append(int(operations[i]))
        for val in stack:
            x+=val
        return x



