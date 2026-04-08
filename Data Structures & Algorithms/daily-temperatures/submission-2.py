class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[] # [[]] format
        for i,v in enumerate(temperatures):
             #popping and adding to results
            while stack and v > stack[-1][0]:
                v1=stack.pop()
                result[v1[1]]=i-v1[1]

            stack.append([v,i])    
        return result
                
        
