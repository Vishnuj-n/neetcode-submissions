class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if not self.stack or val<=self.stack[-1][1]:
            self.stack.append([val,val])
        else:
            cv=self.stack[-1][1]
            self.stack.append([val,cv])    

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
