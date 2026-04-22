class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        dic=Counter(tasks)
        maxHeap = [-cnt for cnt in dic.values()]
        heapq.heapify(maxHeap)
        q=deque()
        while maxHeap or q:
            time+=1
            if maxHeap:
                count=1+heapq.heappop(maxHeap)
                if count:
                    q.append([count,time+n])
            if q and q[0][1]==time:
                value=q.popleft()[0]
                heapq.heappush(maxHeap,value)
        return time