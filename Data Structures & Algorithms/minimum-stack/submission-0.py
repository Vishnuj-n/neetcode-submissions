class MinStack:

    def __init__(self):
        self.s=[]
        self.min1=[]

    def push(self, val: int) -> None:
        if self.s=="MinStack":
            return None
        self.s.append(val)
        if self.min1:
            minval=min(val,self.min1[-1])
        else:
            minval=val
        self.min1.append(minval)
        
        return None

    def pop(self) -> None:
        self.s.pop()
        self.min1.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min1[-1]

        
