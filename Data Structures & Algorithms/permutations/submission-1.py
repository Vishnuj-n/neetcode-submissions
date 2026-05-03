class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        def dfs(i,l):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            if i>=len(nums):
                return
            for v in range(len(nums)):
                if nums[v] in curr:
                    continue
                curr.append(nums[v])
                dfs(i+1,l+1)
                curr.pop()
        dfs(0,0)
        return res