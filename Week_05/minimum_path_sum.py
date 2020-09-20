# 64 最小路径和

class Solution:
    def minPathSum(self, grid):

        row = len(grid)-1
        column = len(grid[0])-1

        for r in range(row, -1, -1):
            for c in range(column, -1, -1):
                if r == row and c == column: continue
                elif c == column:   grid[r][c] = grid[r+1][c] + grid[r][c]
                elif r == row:  grid[r][c] = grid[r][c+1] + grid[r][c]
                else:
                    min_sum = min(grid[r][c+1],grid[r+1][c])
                    grid[r][c] = min_sum + grid[r][c]
        return grid[0][0]