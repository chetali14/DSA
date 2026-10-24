
class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Each land cell has 4 sides
                    perimeter += 4

                    # Shared side with land above
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # Shared side with land to the left
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter
