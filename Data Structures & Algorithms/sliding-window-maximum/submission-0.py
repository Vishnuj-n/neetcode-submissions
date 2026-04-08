class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        state=deque()
        start=0
        op=[]
        for end in range(len(nums)):
            while state and nums[state[-1]] < nums[end]:
                state.pop()
            state.append(end)
            if state[0] < start:
                state.popleft()
                
            if end-start+1==k:
                op.append(nums[state[0]])
                start+=1

        return op