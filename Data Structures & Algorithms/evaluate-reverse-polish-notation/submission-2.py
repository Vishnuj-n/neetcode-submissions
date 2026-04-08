class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        op=["+","-","/","*"]
        

        for i in range(len(tokens)):
            if tokens[i] in op:
                b=s.pop()
                a=s.pop()
                s.append(int(eval(f"{a}{tokens[i]}{b}")))
            else:
                s.append(int(tokens[i]))
        return s[-1]