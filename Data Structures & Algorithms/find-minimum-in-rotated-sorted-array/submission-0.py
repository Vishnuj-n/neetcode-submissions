class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        res = nums[0]
        while l<=h:
            if nums[l]<nums[h]:
                return min(res,nums[l])
            m=(l+h)//2
            res = min(nums[m],res)

            if nums[m]>=nums[l]:
                l=m+1
            else:
                h=m-1
        return res

