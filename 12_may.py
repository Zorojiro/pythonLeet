# You are given an n x n integer matrix grid.

# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

# Return the generated matrix.

# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]



class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]

        for i in range(1, n-1):
            for j in range(1, n-1):
                temp = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        temp = max(temp, grid[k][l])
                res[i-1][j-1] = temp
        
        return res


        