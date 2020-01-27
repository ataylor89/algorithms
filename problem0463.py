class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        numRows = len(grid)
        numCols = len(grid[0])
        
        perimeter = 0
        
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    numConnections = self.countConnections(r, c, grid)
                    perimeter += (4 - numConnections)
                    
        return perimeter
    
    def countConnections(self, r, c, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        
        n = 0
        
        # down
        if r < numRows-1 and grid[r+1][c] == 1:
            n += 1
        # right
        if c < numCols-1 and grid[r][c+1] == 1:
            n += 1
        # up
        if r > 0 and grid[r-1][c] == 1:
            n += 1
        # left
        if c > 0 and grid[r][c-1] == 1:
            n += 1
        
        return n
