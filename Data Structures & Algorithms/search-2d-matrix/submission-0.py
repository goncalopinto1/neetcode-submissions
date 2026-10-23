class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        previous_higher = -1

        for row in matrix: # O(m)
            l = 0
            r = len(row) - 1

            while l <= r:
                middle = (r + l) // 2

                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    l = middle + 1
                else:
                    r = middle - 1

        return False