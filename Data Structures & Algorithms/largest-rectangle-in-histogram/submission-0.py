class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        for i in range(len(heights)):  
            min_val=heights[i]
            for j in range(i,len(heights)):
                min_val=min(min_val,heights[j])
                area=min_val*(j-i+1)
                max_area=max(area,max_area)
        return max_area