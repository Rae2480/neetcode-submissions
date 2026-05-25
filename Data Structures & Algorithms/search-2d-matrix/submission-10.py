class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        

        while up <= down:
            middle = (up + down) // 2
            if matrix[middle][len(matrix[0]) - 1] < target:
                up = middle + 1
            elif matrix[middle][0] > target:
                down = middle - 1
            else:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    mid = (left+right) // 2
                    if matrix[middle][mid] == target:
                        return True
                    elif matrix[middle][mid] < target:
                        left = mid + 1
                    else:
                        right = mid -1
                return False
        return False
