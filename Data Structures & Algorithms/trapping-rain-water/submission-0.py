class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        lmax,rmax = height[l],height[r]
        cont=0
        while l<r:
            if lmax<rmax:
                l+=1
                if height[l]>lmax:
                    lmax=height[l]
                else:
                    cont+=lmax-height[l]
            else:
                r-=1
                if height[r]>rmax:
                    rmax=height[r]
                else:
                    cont+=rmax-height[r]
        
        return cont
                

        