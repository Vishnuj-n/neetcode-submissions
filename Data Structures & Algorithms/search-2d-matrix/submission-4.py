class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, h = 0, m*n - 1
        
        while l <= h:
            mid = (l + h) // 2
            mm = mid // n
            mn = mid % n
            
            if target > matrix[mm][mn]:
                l = mid + 1
            elif target == matrix[mm][mn]:
                return True
            else:
                h = mid - 1
        
        return False

