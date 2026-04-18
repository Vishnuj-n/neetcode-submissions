class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       s=[-i for i in nums]
       heapq.heapify(s)
       print(s)
       while k>0:
        large=heapq.heappop(s)
        k-=1
       return -(large)