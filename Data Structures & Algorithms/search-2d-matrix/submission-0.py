class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R = len(matrix)-1
        L = 0

        while R >= L:
            mid = int((R+L)/2)
            if  target < matrix[mid][0]:
                R = mid-1
            elif matrix[mid][-1] < target:
                L = mid + 1

            else:
                l = 0
                r = len(matrix[mid])-1
                while r >= l:
                    m = int((l+r)/2)

                    if target < matrix[mid][m]:
                        r = m-1
                    elif target > matrix[mid][m]:
                        l = m+1
                    else:
                        return True
                
                break
        
        return False
