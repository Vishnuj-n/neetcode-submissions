class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=m*n-1

        while low<=high:
            mid=(low+high)//2
            mid_m=mid//n 
            mid_n=mid%n
            if matrix[mid_m][mid_n]==target:
                return True
            elif target>matrix[mid_m][mid_n]:
                low=mid+1
            else:
                high=mid-1
        return False


            
