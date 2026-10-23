class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle = (top + bottom) // 2

            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                l = 0
                r = len(matrix[middle]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if matrix[middle][m] == target: 
                        return True
                    elif matrix[middle][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                
                return False
                
        return False
