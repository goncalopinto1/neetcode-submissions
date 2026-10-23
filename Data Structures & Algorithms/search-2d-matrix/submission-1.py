class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix: # O(m)
            if row[-1] == target: return True

            elif row[-1] > target: # esta lesta row
                l = 0
                r = len(row) - 1

                while l <= r:
                    middle = (l + r) // 2

                    if row[middle] == target: 
                        return True
                    elif row[middle] < target:
                        l = middle + 1
                    else:
                        r = middle - 1
                break
            
        return False