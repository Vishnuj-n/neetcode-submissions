class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        n=len(temperatures)
        for i in range(n):
            for j in range(i,n):
                if temperatures[i]<temperatures[j]:
                    result.append(j-i)
                    break
                if j==n-1:
                    result.append(0)
        return result