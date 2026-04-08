class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]<=target and target<=matrix[i][-1]:
                l=0
                h=len(matrix[i])-1
                while l<=h:
                    mid=(l+h)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        l=mid+1
                    else:
                        h=mid-1

        return False
                    

            
