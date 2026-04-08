class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=1
        l=[0]*n
        for i in range(n):
            for j in range(n):
                if nums[j]==0 and j!=i:
                    ans=0
                    break
                if j==i:
                    continue
                else:
                    ans*=nums[j]
            l[i]=ans
            ans=1
        return l

        