from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap1=[]
        for x,y in points:
            dist=(x**2)+(y**2)
            heap1.append([dist,x,y])
        heapq.heapify(heap1)
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(heap1)
            res.append([x,y])
            k-=1
        return res

        

