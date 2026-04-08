class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1
            while(l<r):
                ts=a+nums[l]+nums[r]
                if ts<0:
                    l+=1
                elif ts>0:
                    r-=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res