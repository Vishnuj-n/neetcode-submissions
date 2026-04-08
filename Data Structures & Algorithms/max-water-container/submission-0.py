class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        area=0
        while(l<r):
            lt=r-l
            ht=min(heights[l],heights[r])
            area=max(lt*ht,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return area



